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
            process.StartInfo = startInfo;
            process.Start();
        }

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void axAcroPDF1_Enter(object sender, EventArgs e)
        {

        }

        private void Form1_Resize(object sender, System.EventArgs e)
        {
            //textBox1.MinimumSize = new Size(this.Size.Width / 2, textBox1.Size.Height);
        }

        private void button1_Click(object sender, EventArgs e)
        {
            File.WriteAllText("test.lazytex", textBox1.Text);
            run_cmd("/C python ../../../../../lazylatex.py" + " " + "test.lazytex");
            run_cmd("/C pdflatex output.tex");
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
