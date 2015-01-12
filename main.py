import sys
from forms import MainForm
 
def main():
    token=1
    temperature=36
    alcohol=6.5
    app, mainForm, window = MainForm.init(token,temperature,alcohol)
    window.show()
    sys.exit(app.exec_())
 
if __name__ == "__main__":
    main()
