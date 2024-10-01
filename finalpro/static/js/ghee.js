const base=document.getElementById('base')
const one=document.getElementById('one')
const two=document.getElementById('two')
const three=document.getElementById('three')
const four=document.getElementById('four')
one.addEventListener("click",function(){
 base.textContent=158
    
})
two.addEventListener("click",function(){
    base.textContent=318
       
   })
three.addEventListener("click",function(){
    base.textContent=635
       
   })
four.addEventListener("click",function(){
    base.textContent=1270
       
   })

base.appendChild('one')
base.appendChild('two')
base.appendChild('three')
base.appendChild('four')