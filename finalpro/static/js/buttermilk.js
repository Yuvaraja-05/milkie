const base=document.getElementById('base')
const one=document.getElementById('one')
const two=document.getElementById('two')
const three=document.getElementById('three')
const four=document.getElementById('four')
one.addEventListener("click",function(){
 base.textContent=16
    
})
two.addEventListener("click",function(){
    base.textContent=35
       
   })
three.addEventListener("click",function(){
    base.textContent=70
       
   })
four.addEventListener("click",function(){
    base.textContent=140
       
   })

base.appendChild('one')
base.appendChild('two')
base.appendChild('three')
base.appendChild('four')