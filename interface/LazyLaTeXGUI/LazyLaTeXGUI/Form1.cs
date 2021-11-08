using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.IO;

namespace LazyLaTeXGUI
{
    public partial class Form1 : Form
    {
        private void run_cmd(string args)
        {
            System.Diagnostics.Process process = new System.Diagnostics.Process();
            System.Diagnostics.ProcessStartInfo startInfo = new System.Diagnostics.ProcessStartInfo();
            startInfo.FileName = "cmd.exe";
            startInfo.Arguments = args;
            startInfo.WindowStyle = System.Diagnostics.ProcessWindowStyle.Hidden;
            System.Diagnostics.Process cmd = System.Diagnostics.Process.Start(startInfo);
            cmd.WaitForExit();
        }

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            textBox2.Text = "Please write LazyLaTeX on the left textbox and press 'generate'.";
            button2.Enabled = false;
        }

        private void axAcroPDF1_Enter(object sender, EventArgs e)
        {

        }

        private void Form1_Resize(object sender, System.EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            button2.Enabled = false;
            textBox2.Text = "Generating tex...";
            File.WriteAllText("test.lazytex", textBox1.Text);
            run_cmd("/C python ../../../../../lazylatex.py" + " " + "test.lazytex");
            textBox2.Text = "Tex generated...compiling pdflatex...";
            run_cmd("/C pdflatex output.tex");
            button2.Enabled = true;
            textBox2.Text = "PDF generated. Please press 'show' to display.";
        }

        private void button2_Click(object sender, EventArgs e)
        {
            axAcroPDF1.LoadFile("output.pdf");
        }

        private void tableLayoutPanel1_Paint(object sender, PaintEventArgs e)
        {

        }
    }
}
