class BrowserHistory:

    def __init__(self, homepage: str):
        self.homepage = homepage # keep track of homepage url
        # keep track of visited pages, 2 stacks (back/forward)
        self.bwd = []
        self.fwd = []

    def visit(self, url: str) -> None:
        self.fwd.clear() # clear forward history list
        self.bwd.append(self.homepage) # add current pg to backward history list
        self.homepage = url # update current page

    def back(self, steps: int) -> str:
        if not self.bwd:
            return self.homepage
        while self.bwd and steps > 0:
            self.fwd.append(self.homepage)
            self.homepage = self.bwd.pop()
            steps -= 1
        return self.homepage

    def forward(self, steps: int) -> str:
        if not self.fwd: # no fwd -> return current
            return self.homepage
        while self.fwd and steps > 0:
            self.bwd.append(self.homepage)
            self.homepage = self.fwd.pop()
            steps -= 1
        return self.homepage

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)