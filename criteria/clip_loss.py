
import torch
import clip


class CLIPLoss(torch.nn.Module):

    def __init__(self):
        super(CLIPLoss, self).__init__()
        self.model, self.preprocess = clip.load("ViT-B/32", device="cuda")
        #self.upsample = torch.nn.Upsample(scale_factor=7)
        #self.avg_pool = torch.nn.AvgPool2d(kernel_size=opts.stylegan_size // 32)

    def forward(self, image, text):
        # image = torch.nn.functional.upsample_bilinear(image, (224, 224))
        image = torch.nn.functional.interpolate(image, size=(224, 224), mode='bilinear', align_corners=False)
        #image = self.avg_pool(self.upsample(image))
        similarity = 1 - self.model(image, text)[0] / 100
        return similarity#.mean()
