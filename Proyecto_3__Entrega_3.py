import numpy as np
import matplotlib.pylab as plt

L= 1.04 


def Calculo_matriz(delta_t,malla,Tiempo_final):
    """delta t es el tiempo pasante en segundo
    y malla la cantidad de nodos que se encuentran    """
    L= 1.04  #metros
    n= malla
    dt= float(delta_t)
    Nt= Tiempo_final
    dx= L/n
    dt= delta_t
    x=np.linspace(0,L,n+1)
    Tiempo=np.linspace(0,Nt/3600,int(Nt/dt))
    Nt = int(Nt/dt)
    u= np.zeros((Nt,n+1))
    u_fourier= np.zeros((Nt,n+1))
    #condiciones 
      #   u[:,0]= 0  # izquierda
    u[:,-1]=  20      #derecha
    u[0,0:n]= 20     # temp. inicial
    K = 79.5
    c=450
    rho = 7800
    alpha= K*dt/(c*rho*dx**2)
    
    N_ploteo=1000 
    N_skip=5
    
    for j in range(Nt-1):
        t = dt*j
    
        u[j,0]= -5*dx +u[j,1]
        u[0,0]= 20
            
        for i in range(1,n):
            u[j+1,i]= u[j,i]+  alpha*( u[j,i-1] -  2* u[j,i] +  u[j,i+1])
        
        if dt ==2:
            if j % N_ploteo ==0:
                plt.plot(x,u[j,:])
        
            if j % (N_ploteo*N_skip)==0:
                plt.text(x[0],u[j,0], f"{t/3600:.1f}", fontsize=8, horizontalalignment= "center", verticalalignment="center"
                         ).set_bbox(dict(facecolor="white", alpha=0.4, edgecolor="black", boxstyle="round"))
    
    if dt ==2:
        plt.title(f"k = {j}  t =  {j*dt}")
        plt.ylabel("Temeratura, $T$  [°C]" )
        plt.xlabel("Distancia, $x$ [m]")
        plt.show()
        
    return  (u, Tiempo)






pi= np.pi
e=np.e
def Serie_Fourier(t,x,alpha):
    nn=1
    Temp_f=0
    while True:
        Temp_f +=((40*(1-(-1)**nn))/(nn*pi)*np.sin( (nn*pi*x)/L)  * e**(-alpha*(nn*pi/L )**2*t))
        nn+=1
        if nn==10:
            return  Temp_f
        

# Matriz con la serie de Fouirer
Nt=50000
n=20
K = 79.5
c=450
rho = 7800
dt=1
dx= L/n
alpha= K*dt/(c*rho*dx**2)
x=np.linspace(0,L,n+1)
u_fourier= np.zeros((Nt,n+1))

print (" cuente hasta 20")
for i in range(len(u_fourier[0])):
    print (i)
    for j in range (len(u_fourier)):
        u_fourier[j,i]=abs(Serie_Fourier(j/3600,i,alpha))




a=50000
Tiempo_1=Calculo_matriz(1,20,a)
Tiempo_2=Calculo_matriz(2,20,a)
Tiempo_5=Calculo_matriz(5,20,a)
Tiempo_10=Calculo_matriz(10,20,a)
Tiempo_50=Calculo_matriz(50,20,a)
#Tiempo_100=Calculo_matriz(100,20,a)


a=50040
Malla_10=Calculo_matriz(60,10,a)
Malla_20=Calculo_matriz(60,20,a)
Malla_40=Calculo_matriz(60,40,a)
Malla_60=Calculo_matriz(60,60,a)
Malla_100=Calculo_matriz(60,100,a)



largos={2:"0.104",4:"0.208",8:"0.416"}
l_i=[2,4,8]



for i in l_i:
    plt.figure()
    plt.plot (Tiempo_1[1],Tiempo_1[0][:,l_i],label="Malla 20 Delta_t = 1 [seg]")
    plt.plot (Tiempo_2[1],Tiempo_2[0][:,l_i],label="Malla 20 Delta_t = 2 [seg]")
    plt.plot (Tiempo_5[1],Tiempo_5[0][:,l_i],label="Malla 20 Delta_t = 5 [seg]")
    plt.plot (Tiempo_10[1],Tiempo_10[0][:,l_i],label="Malla 20 Delta_t = 10 [seg]")
    plt.plot (Tiempo_50[1],Tiempo_50[0][:,l_i],label="Malla 20 Delta_t = 50 [seg]")
    #plt.plot (Tiempo_100[1],Tiempo_100[0][:,l_i],label="Malla 20 Delta_t = 100 [seg]")
    plt.plot (Tiempo_1[1],u_fourier[:,l_i],label="prediccion de furier")

    plt.show()
    plt.legend(loc=1)
    plt.title(f" x = {largos[i]} [m]")
    plt.ylabel("Temeratura, $T$  [°C]")
    plt.xlabel("Tiempo  [Horas]")
    plt.show()


for i in l_i:
    plt.figure()
    plt.plot (Malla_10[1],Malla_10[0][:,l_i],label="M10 : Malla 10")
    plt.plot (Malla_20[1],Malla_20[0][:,l_i],label="M20 : Malla 20")
    #plt.plot (Malla_40[1],Malla_40[0][:,l_i],label="M40 : Malla 40")
    #plt.plot (Malla_60[1],Malla_60[0][:,l_i],label="M60 : Malla 60")
    #plt.plot (Malla_100[1],Malla_100[0][:,l_i],label="M100 : Malla 100")
    
    plt.legend(loc=1)
    plt.title(f" x = {largos[i]} [m]")
    plt.ylabel("Temeratura, $T$  [°C]")
    plt.xlabel("Tiempo  [Horas]")
    plt.show()












