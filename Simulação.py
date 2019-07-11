#Iniciamente, iremos declarar as constantes. A partir desses valores, os demais serão determinados.
x0 = float(input("Insira o valor de xo:"))
y0 = float(input("Insira o valor de yo:"))
n1 = float(input("Insira o valor de n1:"))
n2 = float(input("Insira o valor de n2:"))


if (x0>0 or y0<0 or n1<1 or n2<1): #condições importante, pois sem elas o modelo não funcionaria.
    print("Lembre-se que pelo modelo proposto, temos x0<0, y0>0, n1>0, n2>0 e n1<n2!")
else:
    n = n1/n2
    x=(-1)*x0*n
    y= (-1)*((x0**2)*(1-n**2)+y0**2)**(1/2)
    xc=(y0*(x-x0)/(y0-y)) + x0
    yc=0
    
    print("As coordenadas do vetor B=(",x,",",y,").")
    print("As coordenadas do vetor C=(",xc,",",yc,").")

    #vetor AO
    aox = x0 
    aoy = y0
    mao = ((aox)**2 + (aoy)**2)**(1/2)
    print("O módulo do vetor AO é", mao, "m.")

    #vetor OB
    obx = x
    oby = y
    mob = ((obx)**2 + (oby)**2)**(1/2)
    print("O módulo do vetor OB é", mob, "m.")

    #vetor AC
    acx = xc-x0
    acy = yc-y0
    mac = ((acx)**2 + (acy)**2)**(1/2)
    print("O módulo do vetor AC é", mac, "m.")

    #vetor CB
    cbx = x-xc
    cby = y-yc
    mcb = ((cbx)**2 + (cby)**2)**(1/2)
    print("O módulo do vetor CB é", mcb, "m.")
    
    #velocidades
    c=299792458
    v1 = c/n1
    v2 = c/n2
    print("O módulo da velocidade no meio 1 é", v1, "m/s.")
    print("O módulo da velocidade no meio 2 é", v2, "m/s.")

    #intervalos de tempo
    dt1=mao/v1
    dt2=mob/v2
    dt3=mac/v1
    dt4=mcb/v2

    dtr=((mao/v1)+(mob/v2))*(10**9) #real
    dtf=((mac/v1)+(mcb/v2))*(10**9) #em linha reta
    r=dtf/dtr #razão entre o tempo "real" e o tempo "em linha reta".
    print("O intervalo para que a luz percorra o caminho AOB é", dtr, "ns.")
    print("O intervalo para que a luz percorra o caminho ACB é", dtf, "ns.")
    print("A razão entre os dois intervalos de tempo é",r,".")
