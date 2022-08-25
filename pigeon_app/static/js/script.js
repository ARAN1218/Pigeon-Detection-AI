// プレビュー機能
function previewImage(obj)
{
	var fileReader = new FileReader();
	fileReader.onload = (function() {
		document.getElementById('preview').src = fileReader.result;
	});
	fileReader.readAsDataURL(obj.files[0]);
}

// 読み込み画面
window.onload = function() {
	const spinner = document.getElementById('loading');
   
	// Add .loaded to .loading
	spinner.classList.add('loaded');
}


// アコーディオンメニュー
const tabs = document.querySelectorAll(".accordion__tab");
const contents = document.querySelectorAll(".accordion__content");
const test = 1;

for (let i = 0; i < tabs.length; i++) {
  // 質問タブをクリックしたら発火
  tabs[i].addEventListener("click", function () {
    // クリックした質問タブのactiveクラスを付け替える
    tabs[i].classList.toggle("active");
    // クリックした質問タブのindex番号の回答コンテンツのactiveクラスを付け替える
    contents[i].classList.toggle("active");
  });
}