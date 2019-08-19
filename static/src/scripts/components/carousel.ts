import Siema from "siema";

export type CarouselSelectors = { [key: string]: string };

export class CarouselList {
    list: Carousel[] = [];
    constructor(
        public el: string = "[data-carousel]",
    ) {
        this.updateList();
    }
    private updateList(): Carousel[] {
        this.list = [];
        let elements = document.querySelectorAll(this.el);
        elements.forEach(el => {
            this.list.push(new Carousel(el))
        })
        return this.list;
    }
};

export class Carousel {
    ctrl: Siema;
    selectors: CarouselSelectors = {
        track: "[data-carousel-track]",
        prev: "[data-carousel-prev]",
        next: "[data-carousel-next]",
        goto: "[data-carousel-goto]"
    }
    constructor(public el: Element = null) {
        this.init();
    }
    private init():void {
        if (this.el !== null) {
            let track = this.el.querySelector(this.selectors.track);
            if (track !== null) {
                this.ctrl = new Siema({
                    selector: track as HTMLElement,
                    loop: true,
                    onChange: () => {
                        this.activateButton();
                    }
                });
                this.activateButton();
                this.bind();
            }
        }
    }
    private bind() {
        if (typeof this.ctrl !== "undefined") {
            let prev = this.el.querySelector(this.selectors.prev);
            let next = this.el.querySelectorAll(this.selectors.next);
            let goto = this.el.querySelectorAll(this.selectors.goto);
            if (prev !== null)
                prev.addEventListener("click", () => this.ctrl.prev(), false);
            if (next.length > 0) {
                next.forEach(el => {
                    el.addEventListener("click", () => this.ctrl.next(), false);
                });
            }
            if (goto.length > 0) {
                goto.forEach(el => {
                    el.addEventListener("click", e => {
                        let target = e.target as HTMLElement;
                        let value = target.getAttribute(this.selectors.goto.replace(/\[|\]/g,""));
                        if (value !== null) {
                            let index = Number(value);
                            if (isNaN(index) === false) {
                                index = index >> 0;
                                this.ctrl.goTo(index);
                            }
                        }
                    }, false);
                });
            }
        }
    }
    private activateButton(index?: number) {
        if (typeof index !== "number") {
            index = this.ctrl.currentSlide;
            let buttons = this.el.querySelectorAll(this.selectors.goto);
            buttons.forEach(el => {
                el.classList.remove("active");
                let attr = el.getAttribute(this.selectors.goto.replace(/\[|\]/g,""));
                if (Number(attr) === index)
                    el.classList.add("active");
            });
        }
    }
}
