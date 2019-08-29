export type TabsSelectors = { [key: string]: string };

export class TabsList {
    list: Tabs[] = [];
    constructor(
        public el: string = "[data-tab-wrap]",
    ) {
        this.updateList();
    }
    private updateList(): Tabs[] {
        this.list = [];
        let elements = document.querySelectorAll(this.el);
        elements.forEach(el => {
            this.list.push(new Tabs(el))
        })
        return this.list;
    }
}
export class Tabs {
    selectors: TabsSelectors = {
        tab: "[data-tab]",
        panel: "[data-tab-panel]",
    }
    activeClass: string = "active";
    constructor(public el: Element = null) {
        this.bind();
    }
    activate(id: string): boolean {
        if (typeof id === "string" && id !== "") {
            let tab:Element, panel:Element;
            let tabs = this.el.querySelectorAll(this.selectors.tab);
            let panels = this.el.querySelectorAll(this.selectors.panel);
            for (let i = 0; i < tabs.length; i++) {
                if (this.getId(tabs[i]) === id) {
                    tab = tabs[i];
                    break;
                }
            }
            for (let i = 0; i < panels.length; i++) {
                if (this.getId(panels[i]) === id) {
                    panel = panels[i];
                    break;
                }
            }
            if (tab !== null && panel !== null) {
                tabs.forEach(el => el.classList.remove(this.activeClass));
                panels.forEach(el => el.classList.remove(this.activeClass));
                tab.classList.add(this.activeClass);
                panel.classList.add(this.activeClass);
                return true;
            }
            return false;
        }
        return false;
    }
    private getId(el: Element = null): string {
        if (el !== null) {
            let id:string;
            if (el.getAttribute(this.selectors.panel.replace(/\[|\]/g, "")) !== null) {
                id = el.getAttribute(this.selectors.panel.replace(/\[|\]/g, ""));
            } else {
                id = el.getAttribute("href");
                if (id === null)
                    id = el.getAttribute(this.selectors.tab.replace(/\[|\]/g, ""));
                if (id[0] === "#")
                    id = id.substr(1);
            }
            return id;
        }
        return "";
    }
    private bind(): void {
        if (this.el !== null) {
            let tabs = this.el.querySelectorAll(this.selectors.tab);
            tabs.forEach(el => {
                el.addEventListener("click", e => {
                    e.preventDefault();
                    this.activate(this.getId(el));
                });
            })
        }
    }
}
