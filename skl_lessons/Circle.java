public class Circle {
    private double radius;
    private double pi=3.14;
    public static int count;
    
    public Circle(double r){
        setRadius(r);
        count++;
    }

    public Circle(){
        setRadius(1.0);
        count++;
    }

    public Circle(Circle a){
        //makes a deep copy
        setRadius(a.getRadius());
        count++;
    }

    public void setRadius(double r){
        if (r<=0.0){
            System.out.println("The radius needs to be greater than 0");
            radius=1.0;
        }
        else radius=r;
    }

    public double getRadius(){
        return radius;
    }

    public double getPi(){
        return pi;
    }

    public double getArea(){
        return pi*radius*radius;
    }
}