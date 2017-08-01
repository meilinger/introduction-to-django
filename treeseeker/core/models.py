from django.contrib.gis.db import models  # We're importing from gis since we're using a geometry

class TreeSpecies(models.Model):
    """ Describes a single species of tree """
    common_name = models.CharField(max_length=1024, null=True, blank=True)
    genus = models.CharField(max_length=255)
    species = models.CharField(max_length=255)

    def __str__(self):
        return '({} {}) {}'.format(self.genus, self.species, self.common_name or '')

    @staticmethod
    def from_csv(fname):
        """ Loads species information from a CSV (as provided from www.theplantlist.org) """
        import csv
        ret = []
        reader = csv.DictReader(open(fname))
        for r in reader:
            ret.append(TreeSpecies(genus=r['Genus'], species=r['Species']))
        return ret

class TreeSample(models.Model):
    """ Describes a single sample/observation of a tree """
    objects = models.GeoManager()
    geom = models.PointField()  # The physical lat/lon of the tree
    treespecies = models.ForeignKey(TreeSpecies, on_delete=models.CASCADE)
    height = models.DecimalField(null=True, blank=True, max_digits=5, decimal_places=2)
    crown_width = models.DecimalField(null=True, blank=True, max_digits=5, decimal_places=2)
    collected_at = models.DateTimeField(auto_now_add=True)
