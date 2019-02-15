using System;
using System.IO;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace task4
{
    class Program
    {
        static void Main(string[] args)
        {
            string s = (@"C:\Users\admin\Desktop\PP2\task4");            //сохраняем путь в переменной 
            string t = Path.Combine(s, "labka2");                        //дают значение(имя), сохраняют и обьединяют(отправляют в) с указанной папкой
            string p = Path.Combine(s, "labka22");

            Directory.CreateDirectory(t);                              //создают папку с указанным именем
            Directory.CreateDirectory(p);

            string ss = "labka.txt";                                   //дают имя опять
            string tt = Path.Combine(t, ss);                           //сохраняет в созданной папке

            FileStream fs = File.Create(tt);                          //для создания файла
            fs.Close();                                               //закрываем текущий поток
            s = Path.Combine(p, ss);                                  //обьединяет папки
            File.Copy(tt, s);                                         //копирует заданный файл
            File.Delete(@"C:\Users\admin\Desktop\PP2\task4\labka2\labka.txt");  //удаляет файл по заданной пути
        }
    }
}
