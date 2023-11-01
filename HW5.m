% Theta angles
t1 = 0;
t2 = 0;
t3 = -pi/2;
t4 = 0;
t5 = pi/2;
t6 = 0;
q = [t1;t2;t3;t4;t5;t6;];

% Robot dimensions
W2 = 5.4;
W4 = 6.4;
H1 = 156.4;
H2 = 128.4;
H3 = 410.0;
H4 = 208.4;
H5 = 105.9;
H6 = 105.9;
H7 = 61.5;

% {a} vectors
a = [0      0              0;
     0      0          H1+H2;
     0      0       H1+H2+H3;
     0 -W2+W4              0; 
     0      0 H1+H2+H3+H4+H5;
     0 -W2+W4              0;];

% {S_w} vectors
rot = [0  0  1;
       0  1  0;
       0 -1  0;
       0  0 -1;
       0 -1  0;
       0  0 -1;];

% joint types
jt = 'RRRRRR';

% transformation matrix of end-effector
M = [-1  0 0                    0;
      0 -1 0               -W2+W4;
      0  0 1 H1+H2+H3+H4+H5+H6+H7;
      0  0 0                    1;];


[R,p] = FK_PoE(q,a,rot,jt,M)
