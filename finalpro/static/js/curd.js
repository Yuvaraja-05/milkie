const base=document.getElementById('base')
const one=document.getElementById('one')
const two=document.getElementById('two')
const three=document.getElementById('three')
const four=document.getElementById('four')
one.addEventListener("click",function(){
 base.textContent=32
    
})
two.addEventListener("click",function(){
    base.textContent=65
       
   })
three.addEventListener("click",function(){
    base.textContent=130
       
   })
four.addEventListener("click",function(){
    base.textContent=260
       
   })

base.appendChild('one')
base.appendChild('two')
base.appendChild('three')
base.appendChild('four')