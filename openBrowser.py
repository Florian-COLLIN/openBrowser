import sublime
import sublime_plugin
import webbrowser

class OpenBrowserCommand(sublime_plugin.TextCommand):

    def run(self, edit, url):

        selection = ""
        for region in self.view.sel():
            selection += self.view.substr(region)

        webbrowser.open(url % selection)
