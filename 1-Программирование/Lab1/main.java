/**
 * Лабораторная работа №1 по программированию
 * Вариант 4225
 * @author Глеб Игоревич Маликов
 */
public class main {
    public static void main(String[] args) {

        /*
        * Создание массива c типа short с числами от 5 до 15 влючительно
        */
        short[] c = new short[11];
        System.out.println("Массив c: ");
        for (int i = 0; i < c.length; i++) {
            c[i] = (short) (i + 5);
            System.out.print( c[i] + "\t");

        }
        /*
        * Создание массива x типа double с 10 рандомными числами от -3.0 до 4.0
        */
        double[] x = new double[10];
        System.out.println("\n" + "\n" + "Массив x: ");
        for (int i = 0; i < x.length; i++) {
            double x_fill = (Math.random() * 7) - 3;
            /*
            * 7 это диапазон от -3.0 до 4.0
            * x_fill внутри цикла т.к. число от Math.random должно заново генерироваться
            */
            x[i] = x_fill;
            System.out.print(String.format("%.2f", x[i]) + "\t");
        }

        System.out.println("\n" + "\n" + "Двумерный Массив a: (Первый столбец - массив d. Первая строка - массив x)");
        System.out.print("\t");
        for (int i = 0; i < x.length; i++) {
            System.out.print(String.format("%.2f", x[i]) + "\t");
        }
        System.out.println("\n");

        /*
        * Создание массива a типа double размером 11x10
        */
        double[][] a = new double[11][10];
        for (int row = 0; row < 11; row++) {
            System.out.print( c[row] + "\t");
            for (int column = 0; column < 10; column++) {
                if (c[row] == 12) {
                    a[row][column] = Math.cbrt( Math.pow( (Math.cbrt(x[column]) + 1), 2) );
                    System.out.print(String.format("%.2f", a[row][column]) + "\t");
                }
                else if (c[row] == 5 || c[row] == 6 || c[row] == 10 || c[row] == 11 || c[row] == 15) {
                    a[row][column] = Math.exp( Math.pow( ( Math.atan( (x[column] + 0.5) / 7) * (0.25 + Math.cbrt(x[column]) ) ) , Math.atan( (x[column] + 0.5) / 7) ) );
                    System.out.print(String.format("%.2f", a[row][column]) + "\t");
                }
                else {
                    a[row][column] = Math.asin(Math.pow(Math.sin(Math.atan(Math.pow( ( (x[column] + 0.5) / 7), 2))), 2));
                    System.out.print(String.format("%.2f", a[row][column]) + "\t");
                }
            }
            System.out.println(" ");
        }




    }
}