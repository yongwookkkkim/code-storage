public class PartialCircle extends Circle{
    public double angle;

    public double myArea()
    {
        return getRadius()*getRadius()*getPi()*angle/360.0;
    }
}