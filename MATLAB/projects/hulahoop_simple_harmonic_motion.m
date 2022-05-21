clear; clc; close all;

%constants
g=9.81;

%variables
r=0.04;
Rh=0.075;
Rrot=0;
psi=0.005;
mur=0.3;
mus=0.75;
muk=0.5;
theta=pi./6;
omega=4.*pi;

%initial conditions
phidot_0=0;
phi_0=-pi./36;
IC=[phidot_0, phi_0]';

%time interval
t_start=0;
dt=0.01;
t_end=50;
tVec=[t_start:dt:t_end]';

%function handle
odefun = @(t,z) [
-psi.*(Rrot+Rh.*cos(theta)-r).*omega.*omega.*cos((1-r./Rh).*psi).*sin(atan(2..*r.*psi.*tan(z(2))./Rh))./(r.*cos(z(2)));
z(1);
];

%solve via ode45
[time, statematrix] = ode15s(odefun, tVec, IC);
phidot_sol=statematrix(:,1);
phi_sol=statematrix(:,2);

%plotting
figure
plot(time, phi_sol)
hold on
grid on
xlabel('time (s)')
ylabel('y')
title('yea')
legend('$\phi$', '$\dot{\phi}$', 'Interpreter', 'latex')