## The RockPaperScissorGroup presents:
# Rock paper scissors
Integration example of IBM's Bluemix Visual Recognition Tool into
game rock paper scissor.


https://www.ibm.com/watson/developercloud/visual-recognition/api/v3/?python#classify_an_image
https://console.bluemix.net/docs/services/visual-recognition/index.html#about
https://console.bluemix.net/docs/services/visual-recognition/getting-started.html#prerequisites
https://visual-recognition-demo.mybluemix.net/

Example:
curl -X POST --form "images_file=@SteinTest.jpg" --form "parameters=@myparams.json" "https://gateway-a.watsonplatform.net/visual-recognition/api/v3/classify?api_key={api-key}&version=2016-05-20"

