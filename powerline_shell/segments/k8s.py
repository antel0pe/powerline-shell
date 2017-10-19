import subprocess
from ..utils import BasicSegment

class Segment(BasicSegment):
    def add_to_powerline(self):
        powerline = self.powerline
        try:
            p1 = subprocess.Popen(["kubectl", "config", "current-context"], stdout=subprocess.PIPE)
            context = p1.communicate()[0].decode("utf-8").rstrip()
            if len(context) <= 0:
                return
            elif context == 'minikube':
                fg = 2
            elif context == 'will.iptesting.net':
                fg = 11
            else:
                fg = 9
            powerline.append(' %s ' % context,
                            fg,
                            powerline.theme.K8S_BG,
                            separator="")
        except OSError:
            return
