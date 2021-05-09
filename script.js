let url = 'http://34.123.154.196/data.json'
let loadedJSON = null;
function first() {
            alert("hi");
//		loadedJSON = loadJSON('http://34.123.154.196/data.json', tablebuilder(
$.getJSON('http://34.123.154.196/data.json', tablebuilder(data) {

    var table = document.getElementById('table')
    alert("hello");
        for (var i = 0; i < data.length; i++) {
            var row = `<tr>
                        <td>${data[i].product}</td>
                        //<td>${data[i].output}</td>
                        //<td>${data[i].link}</td>
                  </tr>`
            table.innerHTML += row
        }
});
}