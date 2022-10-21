
import skimage.measure
from PIL import Image
from new_clahe_ottimo import *  

class Preprocessing():
    
    def __init__(self, img, name):
        #accetta img formato PIL 
        #se passi path-> img=Image.open(path)
        
        self.img = img
        self.name = name
        self.cl=np.arange(1,31,1)
        self.tl=np.arange(8,34,2)
        self.lab_planes = None

    def get_img(self):
        return self.img

    # def time_crop(self):
    #     temp_crop=timeit.timeit('crop(self)', setup='from preprocessing import crop, self', number=1)
    #     print('idrid crop   Time : ', temp_crop)
    #     return temp_crop
    
    # def time_resize(self):
    #     temp_resize=timeit.timeit('resize(self)', setup='from  preprocessing import resize, self', number=1)
    #     print('idrid crop   Time : ', temp_resize)
    #     return temp_resize

    # def time_clahe(self):
    #     temp_clahe=timeit.timeit('clahe(self)', setup='from  preprocessing import clahe, self,' number=1)
    #     print('idrid crop   Time : ', temp_clahe)
    #     return temp_clahe
        

    def convert_from_cv2_to_image(self, img: np.ndarray) -> Image:
    # return Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
        return Image.fromarray(img)


    def convert_from_image_to_cv2(self, img: Image) -> np.ndarray:
    # return cv2.cvtColor(numpy.array(img), cv2.COLOR_RGB2BGR)
        return np.asarray(img)

    #@profile()
    def crop(self):
        img_width, img_height = self.img.size

        #3 different type of MESSIDOR2 size
        if (img_width == 2240 and img_height == 1488 ):
             crop_width = 1488
             crop_height = 1488
        elif (img_width == 1440 and img_height == 960 ):
             crop_width =  960
             crop_height = 960
        elif (img_width == 2304 and img_height == 1536):
              crop_width =  1536
              crop_height = 1536

        #IDRid
        elif (img_width == 4288 and img_height == 2848):
              self.img=self.convert_from_image_to_cv2(self.img)
              self.img=cv.copyMakeBorder(self.img, 20, 20, 200, 0, cv.BORDER_CONSTANT, None, value = 0)
              self.img=self.convert_from_cv2_to_image(self.img) 
              crop_width =  3475
              crop_height = 3475

        self.img = self.img.crop(((img_width - crop_width) // 2,
                             (img_height - crop_height) // 2,
                             (img_width + crop_width) // 2,
                             (img_height + crop_height) // 2))
        return self.img

    #@profile
    def resize(self):
        h=456
        w=456
        img_copy = self.get_img()
        self.img = img_copy.resize((h,w))
        return self
        
    def split_channel_img(self):
        img = self.convert_from_image_to_cv2(self.img)
        lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
        self.lab_planes = cv.split(lab) # salva i 2 canali rimanenti

    #@profile()
    def clahe(self):       
        self.split_channel_img()
        for tl_i in self.tl:      
            entropy =[]
            curvature=[]
            curv = []
            axis_x = self.cl
            results=[] #ripulisci i valori ottimali ad ogni immagine
            max_tl, max_cl, max_c =[], [], []
            #itera il cl

            for cl_i in self.cl:
                clahe = cv.createCLAHE(clipLimit=cl_i,tileGridSize=(tl_i,tl_i))
                Im_cl = clahe.apply(self.lab_planes[0])
                entropy.append(skimage.measure.shannon_entropy(Im_cl))


            #fitta la funzione
            popt, pcov = curve_fit(gaussian_f, 
                                   axis_x, 
                                   entropy,
                                   maxfev= 5000000)
            a1, b1, c1, a2, b2, c2 = popt   

            #trova la curva max
            curvature=curvature_f(self.cl,entropy)
            max_curv= max(curvature)
            curv.append((max_curv,curvature.index(max_curv)))
            warnings.simplefilter("ignore")
            results.append((tl_i,max_curv,axis_x[curvature.index(max_curv)]))


        #terminato il ciclo tl
        for r in results:
             max_tl.append(r[0])
             max_c.append(r[1])  
             max_cl.append(r[2])

        c_ott=max(max_c)
        index_c= max_c.index(c_ott)
        tl_ott=max_tl[index_c]
        cl_ott=max_cl[index_c]
        
        #applica il clahe con valori ottimi torvati all'immagine selezionata dal for
        clahe_ott = cv.createCLAHE(clipLimit=cl_ott,tileGridSize=(tl_ott,tl_ott))
        img_cl_ott = clahe_ott.apply(self.lab_planes[0])
        lab = cv.merge([img_cl_ott,self.lab_planes[1],self.lab_planes[2]])
        bgr = cv.cvtColor(lab, cv.COLOR_LAB2BGR)

        prep_image = bgr
        return prep_image

    def run(self):
        self.crop()
        self.resize()
        img_prep = self.clahe()
        return img_prep

