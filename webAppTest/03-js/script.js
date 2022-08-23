let uploadProgress = [];

let progressBar = document.getElementById("progress-bar");

function initializeProgress(numfiles) {
    progressBar.value = 0;
    filesDone = 0;
    filesToDo = numfiles;
}

function initializeProgress(numFiles) {
    progressBar.value = 0;
    uploadProgress = [];

    for (let i = numFiles; i > 0; i--) {
        uploadProgress.push(0);
    }
}

function updateProgress(fileNumber, percent) {
    uploadProgress[fileNumber] = percent;
    let total =
        uploadProgress.reduce((tot, curr) => tot + curr, 0) /
        uploadProgress.length;
    progressBar.value = total;
}

let dropArea = document.getElementById("drop-area");
["dragenter", "dragover", "dragleave", "drop"].forEach((eventName) => {
    dropArea.addEventListener(eventName, preventDefaults, false);
});

function preventDefaults(e) {
    e.preventDefault();
    e.stopPropagation();
}

["dragenter", "dragover"].forEach((eventName) => {
    dropArea.addEventListener(eventName, highlight, false);
});
["dragleave", "drop"].forEach((eventName) => {
    dropArea.addEventListener(eventName, unhighlight, false);
});

function highlight(e) {
    dropArea.classList.add("highlight");
}

function unhighlight(e) {
    dropArea.classList.remove("highlight");
}

dropArea.addEventListener("drop", handleDrop, false);

function handleDrop(e) {
    let dt = e.dataTransfer;
    let files = dt.files;

    handleFiles(files);
}
function handleFiles(files) {
    files = [...files];
    initializeProgress(files.length);
    files.forEach(uploadFile);
    files.forEach(previewFile);
}

function uploadFile(file, i) {
    var url = "YOUR URL HERE";
    var xhr = new XMLHttpRequest();
    var formData = new FormData();
    xhr.open("POST", url, true);

    xhr.upload.addEventListener("progress", function (e) {
        updateProgress(i, (e.loaded * 100.0) / e.total || 100);
    });

    xhr.addEventListener("readystatechange", function (e) {
        if (xhr.readyState == 4 && xhr.status == 200) {
            // Done. Inform the user
        } else if (xhr.readyState == 4 && xhr.status != 200) {
            // Error. Inform the user
        }
    });

    formData.append("file", file);
    xhr.send(formData);
}
// this function needs to be reworked to not show preview of image but of text (see below)
function previewFile(file) {
    let reader = new FileReader();
    reader.readAsDataURL(file);
    reader.onloadend = function () {
        let img = document.createElement("img");
        img.src = reader.result;
        document.getElementById("gallery").appendChild(img);
    };
}

// testing
function fileValidation() {
    var fileInput = document.getElementById("file");
    var filePath = fileInput.value;
    var allowedExtensions = /(\.txt)$/i;
    if (!allowedExtensions.exec(filePath)) {
        alert("Please upload file having extensions .txt only.");
        fileInput.value = "";
        return false;
    } else {
        //Image preview
        if (fileInput.files && fileInput.files[0]) {
            var reader = new FileReader();
            reader.onload = function (e) {
                document.getElementById("preview").innerHTML = "";
                document.getElementById("preview").append(e.target.result);
            };
            reader.readAsText(fileInput.files[0]);
        }
    }
}

function previewFile() {
    const content = document.querySelector(".content");
    const [file] = document.querySelector("input[type=file]").files;
    const reader = new FileReader();

    reader.addEventListener(
        "load",
        () => {
            // this will then display a text file
            content.innerText = reader.result;
        },
        false
    );

    if (file) {
        reader.readAsText(file);
    }
}

//testing above

function submit() {
    selectElement = document.querySelector("#location");
    output = selectElement.options[selectElement.selectedIndex].value;
    document.querySelector(".output").textContent = output;
}