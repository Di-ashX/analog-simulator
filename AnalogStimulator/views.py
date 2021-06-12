from django.shortcuts import render, redirect
from django.http import HttpResponse
from matplotlib import pylab
from pylab import *
import PIL, PIL.Image
from io import *
import base64
import numpy as np

def index(request):
    return render(request, 'index.html')

def rl(request):
    return render(request, 'rl.html')

def rc(request):
    return render(request, 'rc.html')

def result(request):
   

    vol = float(request.POST['voltage'])
    res = float(request.POST['Resistance'])
    ind = float(request.POST['Inductance'])

    x=np.linspace(0,25,500)
    y=np.exp(-1*res/ind*x)
    plot(x,vol*(1-y)/res)

    xlabel('Time')
    ylabel('Current')
    title('Time vs Current')
    grid(True)
    # Store image in a string buffer
    buffer = BytesIO()
    canvas = pylab.get_current_fig_manager().canvas
    canvas.draw()
    graphIMG = PIL.Image.frombytes('RGB', canvas.get_width_height(), canvas.tostring_rgb())
    graphIMG.save(buffer, "PNG")
    pylab.close()
    graphic = buffer.getvalue()
    graphic = base64.b64encode(graphic)
    buffer.close()
   
    graphic1 = vol_time1(vol, res, ind)
    return render(request, 'result.html',{'graphic': str(graphic)[2:-1], 'graphic1': str(graphic1)[2:-1]})


    #return HttpResponse (buffer.getvalue(), content_type="Image/png")


def vol_time1(vol, res, ind):
    x=np.linspace(0,25,500)
    y=np.exp(-1*res/ind*x)
    plot(x,vol*y)
    xlabel('Time')
    ylabel('Voltage')
    title('Time vs Voltage')
    grid(True)

    buffer = BytesIO()
    canvas = pylab.get_current_fig_manager().canvas
    canvas.draw()
    graphIMG = PIL.Image.frombytes('RGB', canvas.get_width_height(), canvas.tostring_rgb())
    graphIMG.save(buffer, "PNG")
    pylab.close()
    graphic1 = buffer.getvalue()
    graphic1 = base64.b64encode(graphic1)
    buffer.close()
    #print(graphic1)
    return graphic1





def resultrc(request):
       

    vol = float(request.POST['voltage'])
    res = float(request.POST['Resistance'])
    cap = float(request.POST['Capacitance'])

    x=np.linspace(0,50,500)
    y=np.exp((-1*x)/(res*cap))
    plot(x,vol*y/res)

    xlabel('Time')
    ylabel('Current')
    title('Time vs Current')
    grid(True)
    # Store image in a string buffer
    buffer = BytesIO()
    canvas = pylab.get_current_fig_manager().canvas
    canvas.draw()
    graphIMG = PIL.Image.frombytes('RGB', canvas.get_width_height(), canvas.tostring_rgb())
    graphIMG.save(buffer, "PNG")
    pylab.close()
    graphic = buffer.getvalue()
    graphic = base64.b64encode(graphic)
    buffer.close()
    
    graphic1 = vol_time2(vol, res, cap)
    return render(request, 'resultrc.html',{'graphic': str(graphic)[2:-1], 'graphic1': str(graphic1)[2:-1]})



def vol_time2(vol, res, cap):
    x=np.linspace(0,50,500)
    y=np.exp((-1*x)/(res*cap))
    plot(x,vol*(1-y))
    xlabel('Time')
    ylabel('Voltage')
    title('Time vs Voltage')
    grid(True)

    buffer = BytesIO()
    canvas = pylab.get_current_fig_manager().canvas
    canvas.draw()
    graphIMG = PIL.Image.frombytes('RGB', canvas.get_width_height(), canvas.tostring_rgb())
    graphIMG.save(buffer, "PNG")
    pylab.close()
    graphic1 = buffer.getvalue()
    graphic1 = base64.b64encode(graphic1)
    buffer.close()
    #print(graphic1)
    return graphic1