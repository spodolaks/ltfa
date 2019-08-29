
export class Accordion {
    constructor(
        public selector: string = "[data-accordion]",
        public activeClass: string = "active",
    ) {
        this.bind();
    }
    activate(el: Element, state?: boolean): void {
        if (el !== null) {
            if (typeof state === "boolean") {
                if (state === true)
                    el.classList.add(this.activeClass);
                if (state === false)
                    el.classList.remove(this.activeClass);
            } else {
                el.classList.toggle(this.activeClass);
            }
        }
    }

    private bind() {
        let elements = document.querySelectorAll(this.selector);
        elements.forEach(el => {
            el.addEventListener("click", e => {
                e.preventDefault();
                this.activate(el);
            })
        });
    }
}