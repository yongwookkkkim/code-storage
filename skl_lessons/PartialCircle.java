public class PartialCircle extends Circle{
    private double angle;

    public void setAngle(double angle)
    {
        if (angle<0.0) this.angle=-angle;
        else if (angle==0.0) this.angle=360.0;
        else if (angle>360.0) this.angle=angle%360.0;
        else this.angle=angle;
    }

    public double getAngle()
    {
        return angle;
    }

    public double getArea()
    {
        return getRadius()*getRadius()*getPi()*angle/360.0;
    }

    public double getCircumference()
    {
        return 2.0*getRadius()*getPi()*angle/360.0;
    }

    public double getPerimeter()
    {
        return 2.0*getRadius()*getPi()*angle/360.0+2.0*getRadius();
    }
}