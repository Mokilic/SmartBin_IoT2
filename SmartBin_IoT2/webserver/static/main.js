/*=============== MAIN JS ===============*/ 

initContainer() 

function initContainer(){
       
    containerLiquid = document.querySelector(' .container__liquid')
    containerStatus = document.querySelector('.container__status')
    containerPercentage = document.querySelector('.container__percentage')

    navigator.getBattery().then(() =>{

        updateContainer = () =>{

            containerPercentage.innerHTML = percentageData + '%' 

            containerLiquid.style.height = `${(percentageData)}%`

            if(percentageData <= 30){  
                containerStatus.innerHTML = 'Tom container <i class="ri-delete-bin-7-line green-color"></i>' 
            }
            else if(percentageData <= 60){ 
                containerStatus.innerHTML = 'Masser af plads <i class="ri-delete-bin-4-line animated-yellow"></i>' 
            }
            else if(percentageData <= 90){ 
                containerStatus.innerHTML = 'Snart fuld! <i class="ri-delete-bin-6-line animated-orange"></i>' 
            }
            else{ 
                containerStatus.innerHTML = 'Fuld container <i class="ri-delete-bin-2-line animated-red"></i>' 
            }

            if(percentageData <= 30){ 
                containerLiquid.classList.add('gradient-color-green') 
                containerLiquid.classList.remove('gradient-color-orange','gradient-color-yellow','gradient-color-red') 
            }
            else if(percentageData <= 60){ 
                containerLiquid.classList.add('gradient-color-yellow') 
                containerLiquid.classList.remove('gradient-color-red','gradient-color-orange','gradient-color-green') 
            }
            else if(percentageData <= 90){
                containerLiquid.classList.add('gradient-color-orange')
                containerLiquid.classList.remove('gradient-color-red','gradient-color-yellow','gradient-color-green') 
            }
            else{ 
                containerLiquid.classList.add('gradient-color-red') 
                containerLiquid.classList.remove('gradient-color-green','gradient-color-orange','gradient-color-yellow') 
            }
        }
        updateContainer() 
    })
}