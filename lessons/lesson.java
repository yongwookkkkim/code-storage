public class lesson
{
    public static void main(String args[]){
        int a[] = new int[]{1,2,3,4,5,6};
        int b[] = new int[]{4,-5,9,100,92,-97};
        printElements(a);
        doubleElements(a);
        printElements(a);
        exist(4, a);
        minMax(a);
        int c[]=addition(a, b);
        for (int i=0;i<c.length;i++){
            System.out.println(c[i]);
        }
    }

    public static void printElements(int x[]){
        for (int i=0; i<x.length; i++){
            System.out.println(x[i]);
        }
    }

    public static void doubleElements(int x[]){
        for (int i=0;i<x.length;i++){
            x[i]=2*x[i];
        }
    }

    public static void exist(int a, int[] b){
        boolean exists=false;
        for (int i=0;i<b.length;i++){
            if (b[i]==a){
                exists=true;
            }
        }
        if (exists==true){
            System.out.println("True");
        }
        else{
            System.out.println("False");
        }
    }

    public static void minMax(int x[]){
        int max=0, min=0;
        for (int i=0;i<x.length;i++){
            if (x[i]>max){
                max=x[i];
            }
            else if (x[i]<min){
                min=x[i];
            }
        }
        System.out.println("Max: "+(max)+"\tMin: "+(min));
    }

    public static int[] addition(int a[], int b[]){
        int x[]=new int[a.length];
        for (int i=0;i<a.length;i++){
            x[i]=a[i]+b[i];
        }
        return x;
    }
}