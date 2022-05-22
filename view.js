
function display() {
    let input = document.getElementById('search').value
    document.getElementById('view').innerHTML = null
    fetch("https://6301-169-234-24-177.ngrok.io/generate/" + input)
        .then(
            response => response.json()
        )
        .then(
            result => {
                if (input != "")
                {
                    for(i=1; i<=10; ++i)
                    {
                        document.getElementById('view').innerHTML += '<div class="box">' 
                        + "Song Title: " + result[i][0] 
                        + " → Speed: " + result[i][2].toFixed(1) + '</div> </br >'
                    }
                }
            }
        )
    
    
}

/*
function display() {
    let input = document.getElementById('search').value
    document.getElementById('view').innerHTML = null
    
    if (input != "")
    {
        for(i=1; i<=10; ++i)
        {
            document.getElementById('view').innerHTML += '<div class="box";>' + input + ' ' + i + '</div> </br >'
        }
    }
    
}*/