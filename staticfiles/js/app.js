

const btnTop=document.querySelector(".btntop");
const postID = document.getElementById("post_obj").value;
const likeBtn = document.querySelector('.like-action')
const icon = document.querySelector('.like-action i')
const value = document.querySelector(".ea-1");
const list=document.querySelectorAll(".about-aside-list-item");
const share=document.querySelector(".ea-4")
const links=document.querySelector(".share-toggle")



// Scroll To Top
btnTop.addEventListener("click",function(){
    window.scrollTo({
        top:0,
        left:0,
        behavior:"smooth"
    });
})




//Share 
share.addEventListener("click",function(){

    links.classList.toggle("show-share")

})








//update link number 
likeBtn.addEventListener("click", updateNumberLink)


//get cookie

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');



//create request

function createRequestforLike() {

    let url = '/post/number-of-like';
    var params = { 
    method: 'POST',
    headers: {
        "X-CSRFToken": csrftoken,
        "Accept": "application/json",
        "Content-Type": "application/json"
    },
    body: JSON.stringify({
        'post_id':postID,
    })
    };
    return new Request(url,params);
}


//calculate number of like
function updateNumberLink() {
    
    let request = createRequestforLike()

    fetch(request).then(function(response) {
        return response.json();
    }).then(function(data) {
        if(data['state']==true){
            value.textContent++
            icon.style.color = 'red'
        }else{
            value.textContent--
            icon.style.color = 'rgba(26, 26, 26, 0.4)'
        }
    }).catch(function(ex) {
        console.log("parsing failed", ex);
    });

}





