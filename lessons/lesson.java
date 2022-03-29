public class lesson
{
    public static void main(String[] args){  
        int a[];
        a = new int[] {31,2,3,4,5};
        for (int i=0; i<a.length; i++){
            System.out.println(a[i]);
        }
        System.out.println(fib(10));
    }
    
    public static int fib(int a){
        int res=1, pfib=1, ppfib=0;
        for (int i=1; i<=a-2; i++){
            ppfib=pfib;
            pfib=res;
            res=ppfib+pfib;
        }
        return res;
    }
}