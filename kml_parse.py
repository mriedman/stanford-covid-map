from math import pi,cos
import json

K = 2.5
def coords(x0,y0,x=37.7798,y=-80.3464):
    cc=180/3958/pi/1760*K
    cd=180/3958/pi/1760/cos(x*pi/180)*K
    return [(x0-y)/cd,(x-y0)/cc]
def kml0(f,x=37.7798,y=-80.3464):
    im2=str(open(f).read())
    return kml1(im2,x,y)
def kml1(im2,x=37.7798,y=-80.3464):
    a0,b0=im2.index('<coordinates>'),im2.index('</coordinates>')
    a,b=im2.index('-',a0),len(im2)-1-im2[-1::-1].index(' 0,',len(im2)-1-b0)
    c=[[float(j) for j in i.split(',')[:2]] for i in im2[a:b].split(' ')]
    mm=[200,-200,200,-200]
    for i in c:
        if i[0]<mm[0]:
            mm[0]=i[0]
        if i[0]>mm[1]:
            mm[1]=i[0]
        if i[1]<mm[2]:
            mm[2]=i[1]
        if i[1]>mm[3]:
            mm[3]=i[1]
    if x!=200:
        mm[0]=y
    if y!=200:
        mm[3]=x
    '''cc=180/3958/pi/1760
    cd=180/3958/pi/1760/cos(mm[3]*pi/180)
    c1=[[(i[0]-mm[0])/cd,(mm[3]-i[1])/cc] for i in c]'''
    c1=[coords(i[0],i[1],mm[3],mm[0]) for i in c]
    s='M'
    for i in c1:
        s+=str(round(i[0],4))+' '+str(round(i[1],4))+' L'
    return s[:-2]

def avg_pt(im2,x=37.7798,y=-80.3464):
    a0,b0=im2.index('<coordinates>'),im2.index('</coordinates>')
    a,b=im2.index('-',a0),len(im2)-1-im2[-1::-1].index(' 0,',len(im2)-1-b0)
    c=[[float(j) for j in i.split(',')[:2]] for i in im2[a:b].split(' ')]
    mm=[200,-200,200,-200]
    for i in c:
        if i[0]<mm[0]:
            mm[0]=i[0]
        if i[0]>mm[1]:
            mm[1]=i[0]
        if i[1]<mm[2]:
            mm[2]=i[1]
        if i[1]>mm[3]:
            mm[3]=i[1]
    if x!=200:
        mm[0]=y
    if y!=200:
        mm[3]=x
    '''cc=180/3958/pi/1760
    cd=180/3958/pi/1760/cos(mm[3]*pi/180)
    c1=[[(i[0]-mm[0])/cd,(mm[3]-i[1])/cc] for i in c]'''
    c1=[coords(i[0],i[1],mm[3],mm[0]) for i in c]
    return [round(sum([i[j] for i in c1]) / len(c1), 4) for j in range(2)]

def kml2(im2,x=37.7798,y=-80.3464):
    a0,b0=im2.index('<coordinates>'),im2.index('</coordinates>')
    a,b=im2.index('-',a0),len(im2)-1-im2[-1::-1].index(' 0,',len(im2)-1-b0)
    c=[[float(j) for j in i.split(',')[:2]] for i in im2[a:b].split(' ')]
    mm=[200,-200,200,-200]
    for i in c:
        if i[0]<mm[0]:
            mm[0]=i[0]
        if i[0]>mm[1]:
            mm[1]=i[0]
        if i[1]<mm[2]:
            mm[2]=i[1]
        if i[1]>mm[3]:
            mm[3]=i[1]
    if x!=200:
        mm[0]=y
    if y!=200:
        mm[3]=x
    '''cc=180/3958/pi/1760
    cd=180/3958/pi/1760/cos(mm[3]*pi/180)
    c1=[[(i[0]-mm[0])/cd,(mm[3]-i[1])/cc] for i in c]'''
    c1=[coords(i[0],i[1],mm[3],mm[0]) for i in c]
    c2=[]
    lc1=max(len(c1)-1,2)
    for i in range(lc1):
        c2.append([(c1[i][0]+c1[(i+1)%lc1][0])/2,(c1[i][1]+c1[(i+1)%lc1][1])/2])
    s='M'+str(c2[0][0])+' '+str(c2[0][1])+' Q '+str(c1[1][0])+' '+str(c1[1][1])+' '+str(c2[1][0])+' '+str(c2[1][1])
    for i in c2[2:]+[c2[0]]:
        s+=' T '+str(round(i[0],4))+' '+str(round(i[1],4))
    return s
def kmln(im2,cl,x=37.7798,y=-80.3464):
    a0,b0=im2.index('<coordinates>'),im2.index('</coordinates>')
    a=im2.index('-',a0)
    c=[float(j) for j in im2[a:b0-2].split(' ')[0].split(',')[:2]]
    c1=coords(c[0],c[1],x,y)
    return '<text x="'+str(c1[0]-10)+'px" y="'+str(c1[1])+'px" '+cl+'="n">'+im2.split('<')[0][1:]+'</text>'
def kmle(im2,cl,x=37.7798,y=-80.3464):
    a0,b0=im2.index('<coordinates>'),im2.index('</coordinates>')
    a,b=im2.index('-',a0),len(im2)-1-im2[-1::-1].index(' 0,',len(im2)-1-b0)
    c=[[float(j) for j in i.split(',')[:2]] for i in im2[a:b].split(' ')]
    c1=[coords(i[0],i[1],x,y) for i in c]
    s=''
    #print('a')
    for i in range(0,len(c1),2):
        r=((c1[i][0]-c1[i+1][0])**2+(c1[i][1]-c1[i+1][1])**2)**(1/2)
        #print(r)
        s+='<circle cx="'+str(c1[i][0])+'" cy="'+str(c1[i][1])+'" r="'+str(r)+'" '+cl+'="e" />'
    return s
def p1(l):
    s=''
    for i in l:
        s+='<path class="'+i[0]+'" d="'+kml0('/Users/mriedman/Documents/gp/'+i+'.kml')+'"></path>'
    return s
def p2(l,x=37.7798,y=-80.3464):
    s=''
    cl='class'
    s += f"<image href='stanford-map.png' height='{2540/K}px' width='{2990/K}px' x='{-55/K}px' y='{22/K}px' />"
    for i in l:
        idstr = i.split('<')[0]
        if idstr in places:
            clstr = places[idstr]
        else:
            clstr = ''
        s += '<path ' + cl + '="' + clstr + '" d="' + kml1(i, x, y) + '"></path>'
    for i in l:
        ctr = avg_pt(i, x, y)
        val = names[i.split("<")[0]]
        width = max(len(val), 0)*5/K
        s += f'<text x={ctr[0]-width/2} y={ctr[1]} textLength={width} lengthAdjust=spacingAndGlyphs>{val}</text>'
    k = 6*5/K
    r = 500*5/K
    d = 20*5/K
    s += f'<path d="M{r-k} {d-k} L{r-k} {d+9*3/2*k} L{r+70*5/K} {d+9*3/2*k} L{r+70*5/K} {d-k} z"/>'
    for i in range(9):
        s += f'<path {cl}="ago-{i}" d="M{r} {d+i*k*3/2} L{r+k} {d+i*k*3/2} L{r+k} {d+i*k*3/2+k} L{r} {d+i*k*3/2+k} z" />'
        s += f'<text y="{d+i*k*3/2+20/K}px" x="{r+k+15/K}px" style="font-size:{5*5/K}px;">{str(i)+" days since exposure" if i < 8 else "No exposure"}</text>'
    return f"<svg height='{510*5/K}px' width='{600*5/K}px' style='position:absolute,left:0,top:0,margin:0,z-index:0'>"+s+'</svg>'


def getinfo(gc):
    s=str(open('/Users/mriedman/Library/Application Support/Google Earth/myplaces.kml','r').read())
    s=s[s.index('<name>'+gc+'<'):]
    c,c1=0,0
    for i in range(len(s)):
        if s[i:i+6]=='<Folde':
            c+=1
            c1=2
        if s[i:i+6]=='</Fold':
            c-=1
            if c==-1:
                c1=i
                break
    #s=s[:s.index('</Folder>')]
    s=s[:c1]
    s1=[]
    for i in range(10,len(s)-5):
        if s[i:i+5]=='<name' and s[i+6]!='x':
            #print(s[i+5:i+15])
            s1.append(s[i+6:s[i:].index('</Placema')+i])
    return s1

if __name__ == '__main__':
    gcs=[['stanford-quad-id',37.43808,-122.18458]]
    names = json.load(open('names.json'))
    places = json.load(open('covid-locs.json'))
    #When changing this, also change coords in f(pos) to preserve current location
    st=''
    for i in gcs:
        i[0],a=getinfo(i[0]),i[0]
        st+=p2(*i)
    print(st)
    with open('index.html', 'w') as f:
        f.write('''
    <!DOCTYPE html>
    <html>
        <head>
            <title>Stanford COVID-19 Map</title>
            <style>
                path {
                    fill:#fff;
                    stroke:#000;
                    stroke-width:0.2px;
                    stroke-linecap:round;
                }
                text {
                    font-size:6px;
                    font-family:arial;
                }
                .ago-0 {
                    fill:#d24;
                }
                .ago-1 {
                    fill:#f72;
                }
                .ago-2 {
                    fill:#ea2;
                }
                .ago-3 {
                    fill:#ee2;
                }
                .ago-4 {
                    fill:#6f4;
                }
                .ago-5 {
                    fill:#2ff;
                }
                .ago-6 {
                    fill:#69f;
                }
                .ago-7 {
                    fill:#b9f;
                }
            </style>
        </head>
        <body>''')
        f.write(st)
        f.write('''    </body>
    </html>''')
