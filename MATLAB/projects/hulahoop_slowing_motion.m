clear; clc; close all;

%constants
g=9.81;

%variables
r=0.14;
Rh=0.6;
Rrot=0;
psi=pi./30;
mur=0.3;
mus=0.75;
muk=0.5;

%initial conditions
phidot_0=0;
phi_0=-pi./36;
theta_0=pi./6;
omega_0=6.*pi;
IC=[phidot_0, phi_0, theta_0, omega_0]';

%time interval
t_start=0;
dt=0.1;
t_end=50;
tVec=[t_start:dt:t_end]';

%function handle
odefun = @(t,z) [
-psi.*(Rrot+Rh.*cos(z(3))-r).*z(4).*z(4).*cos((1-r./Rh).*psi).*sin(atan(2..*r.*psi.*tan(z(2))./Rh))./(r.*cos(z(2)));
z(1);
-4.*g.*mur.*cos(z(3)).*(Rh.*cos(z(3))-r).*(Rrot+Rh.*cos(z(3))-r).*z(4).*r./(Rh.*Rh.*(1+cos(z(3)).*cos(z(3))).*(g.*Rh.*sin(z(3))-(Rrot+Rh.*cos(z(3))-r).*Rh.*Rh.*z(4).*z(4)./r./r.*(Rrot+Rh.*cos(z(3))-r)./(cos(z(3)).*cos(z(3)))));
-2.*mur.*cos(z(3)).*(Rh.*cos(z(3))-r).*z(4).*z(4)./(Rh.*(1+cos(z(3)).*cos(z(3))))
];
%to make the graph more visible, the coefficient of dw/dt had been set to
%0.05
%-2.*mur.*cos(z(3)).*(Rh.*cos(z(3))-r).*z(4).*z(4)./(Rh.*(1+cos(z(3)).*cos(z(3))))

%solve via ode45
[time, statematrix] = ode78(odefun, tVec, IC);
phidot_sol=statematrix(:,1);
phi_sol=statematrix(:,2);
theta_sol=statematrix(:,3);
omega_sol=statematrix(:,4);

%plotting
figure
plot(time, phi_sol)
hold on
plot(time, phidot_sol)
plot(time, theta_sol)
plot(time, omega_sol)
grid on
xlabel('time (s)')
ylabel('y')
title('yea')
legend('$\phi$', '$\dot{\phi}$', '$\theta$', '$\omega$', 'Interpreter', 'latex')