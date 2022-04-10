public class lesson
{
    public static void main(String args[]){
        int n=9;
        char a[][] = new char[n][n];

        for (int i=0;i<n*n/3;i++){
            int i1=(int)(Math.random()*n+1.0);
            int i2=(int)(Math.random()*n+1.0);
            if (a[i1][i2]!='*'){
                a[i1][i2]='*';
            }
            else{
                i--;
            }
        }

        for (int i=0;i<n;i++){
            for (int j=0;j<n;j++){
                
            }
        }
    }

}
