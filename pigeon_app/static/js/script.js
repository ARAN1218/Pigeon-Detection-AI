function previewImage(obj)
{
	var fileReader = new FileReader();
	fileReader.onload = (function() {
		document.getElementById('preview').src = fileReader.result;
	});
	fileReader.readAsDataURL(obj.files[0]);
}

window.onload = function() {
	const spinner = document.getElementById('loading');
   
	// Add .loaded to .loading
	spinner.classList.add('loaded');
  }