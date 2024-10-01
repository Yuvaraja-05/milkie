const base=document.getElementById('base')
const one=document.getElementById('one')
const two=document.getElementById('two')
const three=document.getElementById('three')
const four=document.getElementById('four')
one.addEventListener("click",function(){
 base.textContent=32
    
})
two.addEventListener("click",function(){
    base.textContent=75
       
   })
three.addEventListener("click",function(){
    base.textContent=149
       
   })
four.addEventListener("click",function(){
    base.textContent=395
       
   })

base.appendChild('one')
base.appendChild('two')
base.appendChild('three')
base.appendChild('four')