class Lesson
{
    public static void main(String args[]){
        Circle a=new Circle();
        System.out.println("we have "+Circle.count+" instances rn");

        Circle b=new Circle();
        System.out.println("we have "+Circle.count+" instances rn");

        PartialCircle c = new PartialCircle();
        c.setRadius(100.0);
        c.setAngle(-30);
        System.out.println(c.getRadius());
        System.out.println(c.perimeter());
        System.out.println(c.circumference());
        System.out.println(c.getAngle());
    }
}