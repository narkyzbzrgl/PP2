using System;
using System.IO;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace task2
{
    class Program
    {
        public static bool isprime(int b)
        {
            if (b == 1)
            {
                return false;
            }
            for (int i = 2; i * i <= b; ++i)
            {
                if (b % i == 0)
                {
                    return false;
                }
            }
            return true;
        }
        static void Main(string[] args)
        {
            StreamReader s = new StreamReader(@"C:\Users\admin\Desktop\PP2\task2\task2i.txt");   //Стримридер для чтения файла
            StreamWriter st = new StreamWriter(@"C:\Users\admin\Desktop\PP2\task2\task2o.txt");    //Стримрайтер для записи в текстовой файл
            string[] t = s.ReadToEnd().Split();                                                 //читает до конца каждого элемента раздельно 
            int[] a = new int[t.Length];
            for (int i = 0; i < t.Length; i++)
            {
                a[i] = int.Parse(t[i]);                                                         //string like int
            }
            for (int i = 0; i < t.Length; i++)
            {
                if (isprime(a[i]) == true)
                {
                    st.Write(a[i] + " ");
                }
            }
            st.Close();
        }

    }
}