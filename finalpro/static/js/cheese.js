const base=document.getElementById('base')
const one=document.getElementById('one')
const two=document.getElementById('two')
const three=document.getElementById('three')
const four=document.getElementById('four')
one.addEventListener("click",function(){
 base.textContent=120
    
})
two.addEventListener("click",function(){
    base.textContent=250
       
   })
three.addEventListener("click",function(){
    base.textContent=500
       
   })
four.addEventListener("click",function(){
    base.textContent=1000
       
   })

base.appendChild('one')
base.appendChild('two')
base.appendChild('three')
base.appendChild('four')