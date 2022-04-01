public class lesson
{
    public static void main(String args[]){
        int a[] = new int[]{1,2,3,4,5,6};
        int b[] = a;
        printElements(a);
        printElements(b);
        a[1]=8;
        printElements(a);
        printElements(b);
    }

    public static void printElements(int x[]){
        for (int i=0; i<x.length; i++){
            System.out.println(x[i]);
        }
    }
}