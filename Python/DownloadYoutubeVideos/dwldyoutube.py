import pafy

url="https://www.youtube.com/watch?v=i_NmPv5WQ0U&list=RDi_NmPv5WQ0U&start_radio=1" //youtube url

video=pafy.new(url)

best=video.getbest()

best = video.getbest(preftype="mp4")

filename = best.download(filepath="Videos") 
