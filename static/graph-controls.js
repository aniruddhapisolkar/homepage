/* Interactive camera for Leafpress's SVG knowledge graph. */
(() => {
  "use strict";
  const body = document.getElementById("lp-graph-panel-body");
  if (!body) return;

  const panel = body.closest(".lp-graph-panel");
  const controls = document.createElement("div");
  controls.className = "ani-graph-controls";
  controls.setAttribute("role", "group");
  controls.setAttribute("aria-label", "Graph view controls");
  const button = (text, label) => {
    const el = document.createElement("button");
    el.type = "button";
    el.textContent = text;
    el.setAttribute("aria-label", label);
    el.title = label;
    controls.appendChild(el);
    return el;
  };
  const minus = button("−", "Zoom out");
  const percent = document.createElement("span");
  percent.className = "ani-graph-zoom";
  percent.textContent = "100%";
  controls.appendChild(percent);
  const plus = button("+", "Zoom in");
  const reset = button("Reset", "Reset graph view");
  panel.appendChild(controls);

  let attached = null;
  function attach(svg) {
    if (svg === attached) return;
    const box = svg.viewBox.baseVal;
    if (!box.width || !box.height) return;
    attached = svg;
    const initial = { x: box.x, y: box.y, width: box.width, height: box.height };
    let view = { ...initial };
    const pointers = new Map();
    let moved = false;
    let suppressClick = false;
    svg.setAttribute("tabindex", "0");
    svg.setAttribute("aria-label", "Knowledge graph. Drag to pan, scroll or pinch to zoom. Use arrow keys, plus, minus, and zero.");
    svg.classList.add("ani-interactive-graph");

    function render() {
      svg.setAttribute("viewBox", [view.x, view.y, view.width, view.height].join(" "));
      const scale = initial.width / view.width;
      percent.textContent = Math.round(scale * 100) + "%";
      minus.disabled = scale <= 0.35 + 0.001;
      plus.disabled = scale >= 5 - 0.001;
    }
    function point(x, y) {
      const matrix = svg.getScreenCTM();
      if (!matrix) return null;
      const p = svg.createSVGPoint();
      p.x = x;
      p.y = y;
      return p.matrixTransform(matrix.inverse());
    }
    function pan(from, to) {
      const a = point(from.x, from.y);
      const b = point(to.x, to.y);
      if (!a || !b) return;
      view.x -= b.x - a.x;
      view.y -= b.y - a.y;
      render();
    }
    function zoom(factor, anchor) {
      if (!anchor) return;
      const scale = initial.width / view.width;
      const next = Math.max(0.35, Math.min(5, scale * factor));
      const ratio = scale / next;
      view.x = anchor.x - (anchor.x - view.x) * ratio;
      view.y = anchor.y - (anchor.y - view.y) * ratio;
      view.width *= ratio;
      view.height *= ratio;
      render();
    }
    function center() {
      return { x: view.x + view.width / 2, y: view.y + view.height / 2 };
    }
    function resetView() {
      view = { ...initial };
      render();
    }
    minus.onclick = () => zoom(1 / 1.25, center());
    plus.onclick = () => zoom(1.25, center());
    reset.onclick = resetView;
    svg.addEventListener("wheel", event => {
      event.preventDefault();
      const delta = event.deltaY * (event.deltaMode === 1 ? 16 : event.deltaMode === 2 ? 120 : 1);
      zoom(Math.exp(-Math.max(-350, Math.min(350, delta)) * 0.002), point(event.clientX, event.clientY));
    }, { passive: false });

    const midpoint = (a, b) => ({ x: (a.x + b.x) / 2, y: (a.y + b.y) / 2 });
    const distance = (a, b) => Math.hypot(a.x - b.x, a.y - b.y);
    svg.addEventListener("pointerdown", event => {
      if (event.pointerType === "mouse" && event.button !== 0) return;
      if (!pointers.size) {
        moved = false;
        suppressClick = false;
      }
      const pos = { x: event.clientX, y: event.clientY };
      pointers.set(event.pointerId, { ...pos, start: pos });
      if (pointers.size > 1) moved = true;
    });
    svg.addEventListener("pointermove", event => {
      const previous = pointers.get(event.pointerId);
      if (!previous) return;
      const before = [...pointers.values()];
      const next = { x: event.clientX, y: event.clientY, start: previous.start };
      pointers.set(event.pointerId, next);
      const after = [...pointers.values()];
      if (!moved && distance(next, previous.start) < 5) return;
      moved = true;
      svg.classList.add("ani-graph-dragging");
      for (const id of pointers.keys()) {
        try { svg.setPointerCapture(id); } catch (_) { /* pointer may have ended */ }
      }
      if (after.length === 2) {
        const oldMid = midpoint(before[0], before[1]);
        const newMid = midpoint(after[0], after[1]);
        const oldDistance = distance(before[0], before[1]);
        pan(oldMid, newMid);
        if (oldDistance > 1) zoom(distance(after[0], after[1]) / oldDistance, point(newMid.x, newMid.y));
      } else if (after.length === 1) {
        pan(previous, next);
      }
    });
    function finish(event) {
      if (!pointers.has(event.pointerId)) return;
      pointers.delete(event.pointerId);
      if (!pointers.size) {
        suppressClick = moved;
        svg.classList.remove("ani-graph-dragging");
      }
    }
    svg.addEventListener("pointerup", finish);
    svg.addEventListener("pointercancel", finish);
    svg.addEventListener("lostpointercapture", finish);
    svg.addEventListener("pointerleave", event => {
      if (!svg.hasPointerCapture(event.pointerId)) finish(event);
    });
    svg.addEventListener("click", event => {
      if (!suppressClick) return;
      event.preventDefault();
      event.stopImmediatePropagation();
      suppressClick = false;
    }, true);
    svg.addEventListener("keydown", event => {
      const step = view.width * 0.08;
      switch (event.key) {
        case "+": case "=": zoom(1.25, center()); break;
        case "-": zoom(1 / 1.25, center()); break;
        case "0": resetView(); break;
        case "ArrowLeft": view.x -= step; render(); break;
        case "ArrowRight": view.x += step; render(); break;
        case "ArrowUp": view.y -= step; render(); break;
        case "ArrowDown": view.y += step; render(); break;
        default: return;
      }
      event.preventDefault();
    });
    render();
  }
  function findGraph() {
    const svg = body.querySelector("svg");
    if (svg) attach(svg);
  }
  new MutationObserver(findGraph).observe(body, { childList: true });
  findGraph();
})();
