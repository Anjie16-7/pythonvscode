import streamlit as st 
import pandas as pd
import webbrowser
import plotly.express as px
videolink= "videoviews.csv"
try:
    videoviews= pd.read_csv('videoviews.csv')

except:
    videoviews= pd.DataFrame()

menu= st.sidebar.selectbox("Menu", ['Categories','Ratings'])
if menu=="Categories":
    cats=st.sidebar.pills("Choose Category:",['All','Education','Animals','Space','Sport','Music'],default='All')

    if cats=='All' or cats=='Education':
        st.subheader("Educational")
        vd1,vd2,vd3=st.columns(3)
        with vd1:
            st.image("https://luckylittlelearners.com/wp-content/uploads/2023/08/Verb-Tenses-cover.jpg")
            st.write("Learn Verb Tenses")
            if st.button("Play Video",key='1'):
                webbrowser.open("https://youtu.be/cGb4qwKV-to?si=OxKOgN_u1wNZjAuU")
                try:

                    videoviews.loc[0,"Learn Verb Tenses"]+=1
                    videoviews.to_csv(videolink,index=False )
                except:
                    videoviews.loc[0,'Learn Verb Tenses']=1
                    videoviews.to_csv(videolink,index=False )
        with vd2:
            st.image("https://cdn.mos.cms.futurecdn.net/uVwrSjfVvkGwk9y6zNJMob.jpg")
            st.write("Solar System")
            if st.button("Play Video",key='2'):
                webbrowser.open("https://youtu.be/ErUZVWUP0c4?si=dMLd1u5CriTYsmSM")
                try:
                    videoviews.loc[0,"Solar System"]+=1
                    videoviews.to_csv(videolink,index=False )
                except:
                    videoviews.loc[0,'Solar System']=1
                    videoviews.to_csv(videolink,index=False )
        with vd3:
            st.image("https://i.ytimg.com/vi/5iTOphGnCtg/hq720.jpg?sqp=-oaymwEhCK4FEIIDSFryq4qpAxMIARUAAAAAGAElAADIQj0AgKJD&rs=AOn4CLD3b70iq8hohw605nEB622Q_mzzfg")
            st.write("General Chemistry")
            if st.button("Play Video",key='3'):
                webbrowser.open("https://youtu.be/5iTOphGnCtg?si=XElrOj7Bx-YrR8LS")
                try:
                    videoviews.loc[0,"General Chemistry"]+=1
                    videoviews.to_csv(videolink,index=False )
                except:
                    videoviews.loc[0,'General Chemistry']=1
                    videoviews.to_csv(videolink,index=False )
        vd4,vd5,vd6=st.columns(3)
        with vd4:
            st.image("https://www.helpguide.org/wp-content/uploads/2023/02/Laughter.jpeg")
            st.write("Why We Laugh?")
            if st.button("Play Video",key='4'):
                webbrowser.open("https://youtu.be/Xu-QfE_1ksk?si=4_myCKKIzVLYbhi5")
                try:
                    videoviews.loc[0,"Why We Laugh?"]+=1
                    videoviews.to_csv(videolink,index=False )
                except:
                    videoviews.loc[0,'Why We Laugh?']=1
                    videoviews.to_csv(videolink,index=False )
        with vd5:
            st.image("https://webassets.oxfamamerica.org/media/images/Big-Oil-respo.2e16d0ba.fill-1180x738-c100.jpegquality-60.jpg")
            st.write("Climate Change")
            if st.button("Play Video",key='5'):
                webbrowser.open("https://youtu.be/myZAvqqp9Jc?si=I8F9EX0zO_wXEkxK")
                try:
                    videoviews.loc[0,"Climate Change"]+=1
                    videoviews.to_csv(videolink,index=False )
                except:
                    videoviews.loc[0,'Climate Change']=1
                    videoviews.to_csv(videolink,index=False )
        with vd6:
            st.image("https://cdn1.i-scmp.com/sites/default/files/styles/1200x800/public/images/methode/2019/03/01/2a632684-3c00-11e9-a334-8d034d5595df_image_hires_182228.jpg?itok=hXgwquyJ&v=1551435753")
            st.write("Taxes 101")
            if st.button("Play Video",key='6'):
                webbrowser.open("https://youtu.be/Cox8rLXYAGQ?si=VlyMsyYuHsINsy5h")
                try:
                    videoviews.loc[0,"Taxes 101"]+=1
                    videoviews.to_csv(videolink,index=False )
                except:
                    videoviews.loc[0,'Taxes 101']=1
                    videoviews.to_csv(videolink,index=False )
    if cats=="All" or cats=="Animals":
        st.subheader("Animals")
        am1,am2,am3=st.columns(3)
        with am1:
            st.image("https://cdn.britannica.com/29/150929-050-547070A1/lion-Kenya-Masai-Mara-National-Reserve.jpg")
            st.write("Kings Of The Jungle")
            if st.button("Play Video",key='7'):
                webbrowser.open("https://youtu.be/v7GOSYDu-mo?si=jO2d7WJclOXW-iwM")
                try:
                    videoviews.loc[0,"Kings Of The Jungle"]+=1
                    videoviews.to_csv(videolink,index=False )
                except:
                    videoviews.loc[0,'Kings Of The Jungle']=1
                    videoviews.to_csv(videolink,index=False )
        with am2:
            st.image("https://images.unsplash.com/photo-1497752531616-c3afd9760a11?fm=jpg&q=60&w=3000&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8M3x8YmFieSUyMGFuaW1hbHN8ZW58MHx8MHx8fDA%3D")
            st.write("Baby Animals")
            if st.button("Play Video",key='8'):
                webbrowser.open("https://youtu.be/oRDRfikj2z8?si=z-J5MybIbkOM3dGH")
                try:
                    videoviews.loc[0,"Baby Animals"]+=1
                    videoviews.to_csv(videolink,index=False )
                except:
                    videoviews.loc[0,'Baby Animals']=1
                    videoviews.to_csv(videolink,index=False )
        with am3:
            st.image("https://media.istockphoto.com/id/1407655089/photo/funny-pomeranian-dog-summer-ready-for-bath-wrapped-with-a-towel-and-sunglasses-isolated-on.jpg?s=612x612&w=0&k=20&c=wCmR5IKoVVTm5NQY9UL2hBTTkU0AvlG3gnEK8AWUWr8=")
            st.write("Funniest Pets")
            if st.button("Play Video",key='9'):
                webbrowser.open("https://youtu.be/PRAMFqh49b0?si=982raN-BcjlfSlJH")
                try:
                    videoviews.loc[0,"Funniest Pets"]+=1
                    videoviews.to_csv(videolink,index=False )
                except:
                    videoviews.loc[0,'Funniest Pets']=1
                    videoviews.to_csv(videolink,index=False )
        am4,am5,am6=st.columns(3)
        with am4:
            st.image("https://i.ytimg.com/vi/r9PeYPHdpNo/maxresdefault.jpg")
            st.write("Our Planet")
            if st.button("Play Video",key='10'):
                webbrowser.open("https://youtu.be/JkaxUblCGz0?si=2GEFQp6rOvPVqwI1")
                try:
                    videoviews.loc[0,"Our Planet"]+=1
                    videoviews.to_csv(videolink,index=False )
                except:
                    videoviews.loc[0,'Our Planet']=1
                    videoviews.to_csv(videolink,index=False )
        with am5:
            st.image("https://images.fineartamerica.com/images/artworkimages/mediumlarge/2/jungle-life-ferran-vega-vallribera.jpg")
            st.write("Life At Equator")
            if st.button("Play Video",key='11'):
                webbrowser.open("https://youtu.be/ZCYDe0mU2Iw?si=a_T1DiCB-OWcTsd5")
                try:
                    videoviews.loc[0,'Life At Equator']+=1
                    videoviews.to_csv(videolink,index=False )
                except:
                    videoviews.loc[0,'Life At Equator']=1
                    videoviews.to_csv(videolink,index=False )

        with am6:
            st.image("https://www.cbc.ca/kids/images/wild_and_wonderful_asian_animals_header_1140.jpg")
            st.write("Animals In Asia")
            if st.button("Play Video",key='12'):
                webbrowser.open("https://youtu.be/fKmqkGoHWtc?si=ZY3MbuFp5exScEJJ")
                try:
                    videoviews.loc[0,"Animals In Asia"]+=1
                    videoviews.to_csv(videolink,index=False )
                except:
                    videoviews.loc[0,'Animals In Asia']=1
                    videoviews.to_csv(videolink,index=False )
    if cats=='All'or cats=='Space':
        st.subheader("Space")
        sp1,sp2,sp3=st.columns(3)
        with sp1:
            st.image("https://wallpapers.com/images/featured/space-sjryfre8k8f6i3ge.jpg")
            st.write("Space Facts")
            if st.button("Play Video",key='13'):
                webbrowser.open("https://www.youtube.com/live/VIJ-Se52KjY?si=nKlcs2pnyNm0L2wd")
                try:
                    videoviews.loc[0,"Space Facts"]+=1
                    videoviews.to_csv(videolink,index=False )
                except:
                    videoviews.loc[0,'Space Facts']=1
                    videoviews.to_csv(videolink,index=False )
        with sp2:
            st.image ("https://www.funkidslive.com/wp-content/uploads/2022/01/solar-system-5611038_1280.png")
            st.write("Our System")
            if st.button("Play Video",key='14'):
                webbrowser.open("https://youtu.be/Vb2ZXRh74WU?si=18zO3IAyN9E5wP-2")
                try:
                    videoviews.loc[0,"Our System"]+=1
                    videoviews.to_csv(videolink,index=False )
                except:
                    videoviews.loc[0,'Our System']=1
                    videoviews.to_csv(videolink,index=False )
        with sp3:
            st.image("https://static.scientificamerican.com/dam/m/21a318c0da67e978/original/2WYF3N2web.jpg?m=1740673069.305&w=600")
            st.write("Space Station- How it works")
            if st.button("Play Video",key='15'):
                webbrowser.open("https://youtu.be/SGP6Y0Pnhe4?si=ydoIZ1qEHsApWxnK")
                try:
                    videoviews.loc[0,"Space Station- How it works"]+=1
                    videoviews.to_csv(videolink,index=False )
                except:
                    videoviews.loc[0,'Space Station- How it works']=1
                    videoviews.to_csv(videolink,index=False )
        sp4,sp5,sp6=st.columns(3)
        with sp4:
            st.image ("https://i.ytimg.com/vi/BYVZh5kqaFg/hq720.jpg?sqp=-oaymwEhCK4FEIIDSFryq4qpAxMIARUAAAAAGAElAADIQj0AgKJD&rs=AOn4CLBv2YHvPRaK3nFr7WboOZdrKLTvAw")
            st.write("Egg Drop From Space")
            if st.button("Play Video",key='16'):
                webbrowser.open("https://youtu.be/BYVZh5kqaFg?si=l4COur2mzjWDuDDm")
                try:
                    videoviews.loc[0,"Egg Drop From Space"]+=1
                    videoviews.to_csv(videolink,index=False )
                except:
                    videoviews.loc[0,'Egg Drop From Space']=1
                    videoviews.to_csv(videolink,index=False )
        with sp5:
            st.image ("https://starwalk.space/gallery/images/what-is-space/1920x1080.jpg")
            st.write("Mysteries Of Space")
            if st.button("Play Video",key='17'):
                webbrowser.open("https://youtu.be/_NK2g8yStHM?si=fCSMJ0fJ2dPQ_I4C")
                try:
                    videoviews.loc[0,"Mysteries Of Space"]+=1
                    videoviews.to_csv(videolink,index=False )
                except:
                    videoviews.loc[0,'Mysteries Of Space']=1
                    videoviews.to_csv(videolink,index=False )
        with sp6:
            st.image ("https://www.bu.edu/files/2022/07/feat-STScI-01G7ETNMR8CBHQQ64R4CVA1E6T.jpg")
            st.write("Quantums Of Our Universe")
            if st.button("Play Video",key='18'):
                webbrowser.open("https://youtu.be/t06aTX9jM34?si=PaJFzWhldShtjWvc")
                try:
                    videoviews.loc[0,"Quantums Of Our Universe"]+=1
                    videoviews.to_csv(videolink,index=False )
                except:
                    videoviews.loc[0,'Quantums Of Our Universe']=1
                    videoviews.to_csv(videolink,index=False )
    if cats=="All" or cats=="Sport":
        st.subheader("Sports")
        c1,c2,c3=st.columns(3)
        with c1:
            st.image ("https://thedailytexan.com/wp-content/uploads/2021/12/DP8A1058-900x600.jpg")
            st.write("Best Sport Fails")
            if st.button("Play Video",key='19'):
                webbrowser.open("https://youtu.be/cdmKVXynX3I?si=ogtXAkmZnSJkQMtK")
                try:
                    videoviews.loc[0,"Best Sport Fails"]+=1
                    videoviews.to_csv(videolink,index=False )
                except:
                    videoviews.loc[0,'Best Sport Fails']=1
                    videoviews.to_csv(videolink,index=False )

if menu=='Ratings':
    #st.table(videoviews)
    melt_table = videoviews.melt(var_name='Video Title', value_name='Number of Plays')
  #  st.table(melt_table)
    choose=st.radio("Show Data",["Bar","Pie"],horizontal=True)
    if choose=="Bar":
        chart= px.bar(melt_table, x= "Video Title",y="Number of Plays")
        st.plotly_chart(chart)
    if choose=="Pie":
        pie=px.pie(melt_table,names="Video Title",values= "Number of Plays")
        st.plotly_chart(pie)


