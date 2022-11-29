function done1(f,b,c,d)
{
var s_lbl='$$$STARTstatus$$$';
var e_lbl='$$$END$$$';
var nnn=f.elements.length/2-1;
var k=nnn*2+1;
var i;
f.action=d;
f.elements[k].value=s_lbl;

for(i=0;i<nnn;i++)
{

if(f.elements[i*2+2].checked==true)
	{
	f.elements[k].value+='{AK,'+b+','+f.elements[i*2+1].value+',SUCCESS\r\n';
	}

}

f.elements[k].value+='{SS,'+b+',AQ,B'+'\r\n';
f.elements[k].value+='{AL,'+b+',GT'+'\r\n';


f.elements[k].value+=e_lbl;

if(document.bgColor=='#7f7f7f')return;
document.bgColor='#7F7F7F';

f.submit();
}

