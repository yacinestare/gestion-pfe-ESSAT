# -*- coding: utf-8 -*-

from openerp import models, fields, api

# class gestion__pfe(models.Model):
#     _name = 'gestion__pfe.gestion__pfe'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100
class Etudiant(models.Model):
    _name = 'etudiant'

    nom_etu = fields.Char("nom etudiant",help="etudiant nom", required=True)
    prenom_etu=fields.Char("prenom ", required=True)
    date_naiss=fields.Date("date de naissance ", required=True)
    num = fields.Integer('numero')

    image = fields.Binary(string="etudiant image")
    encadrant_id = fields.Many2one("encadrant")
    pfe_id = fields.Many2one("pfe")
    soutenance_id = fields.Many2one("soutenance")

class Encadrant(models.Model):
    _name = 'encadrant'

    nom_enc = fields.Char("nom encadrant",help="encadrant nom", required=True)
    prenom_enc=fields.Char("prenom ", required=True)
    num = fields.Integer('numero')
    image = fields.Binary(string="encadrant image")


    etudiant_ids = fields.One2many("etudiant","encadrant_id")
    pfe_id = fields.Many2one("pfe")
    soutenance_id =fields.Many2many("soutenance")

class Jury(models.Model):
    _name = 'jury'


    nom_ju = fields.Char("nom jury",help="jury nom", required=True)
    prenom_ju=fields.Char("prenom ", required=True)
    num = fields.Integer('numero')
    image = fields.Binary(string="jury image")


    evaluation_ids = fields.Many2many("evaluation")
    soutenance_id = fields.Many2one("soutenance")


class Scolarite(models.Model):
    _name = 'scolarite'

    nom_em = fields.Char("nom employer",help="employer nom", required=True)
    prenom_em=fields.Char("prenom ", required=True)

    pfe_id = fields.Many2one("pfe")


class PFE(models.Model):
    _name = 'pfe'

    titre = fields.Char("titre de PFE", help=" quel le thème ")
    dat_debut = fields.Char("la date de debut pour choisir le theme ", help="dater", required=True)
    dat_depot = fields.Char("la date de dépot du PFE", required=True)
    etudiant_ids = fields.One2many("etudiant","pfe_id")

    encadrant_id = fields.One2many("encadrant","pfe_id")
    scolarite_ids = fields.One2many("scolarite","pfe_id")
    soutenance_id = fields.One2many("soutenance","pfe_id")
    evaluation_ids = fields.One2many("evaluation","pfe_id")
    entreprise_ids = fields.One2many("entreprise","pfe_id")
    pdf = fields.Binary(string="pfe pdf")
    branche_ids = fields.One2many("branche", "pfe_id")


class Soutenance(models.Model):
    _name = 'soutenance'

    date_sout = fields.Date("La date de la soutenance", help="la date de soutence", required=True)
    heur_debut = fields.Char("heur de depart de la soutenance", help=" heur depart ")
    heur_fin = fields.Char("heur de fin de la soutenance", help=" heur fin ")
    etudiant_ids = fields.One2many("etudiant","soutenance_id")
    encadrant_id = fields.Many2many("encadrant")
    pfe_id = fields.Many2one("pfe")
    jury_ids = fields.One2many("jury","soutenance_id")

class Evaluation(models.Model):
    _name = 'evaluation'

    note_eva = fields.Float("la note ", required=True)
    commentaire = fields.Char("le montion ", required=True)


    pfe_id = fields.Many2one("pfe")
    jury_ids = fields.Many2many("jury")


class Entreprise(models.Model):
    _name = 'entreprise'

    nom_ent = fields.Char("nom entreprise ", required=True)
    lieu = fields.Char("le lieu ou setrouve entreprise ", required=True)
    nom_resp = fields.Char("nom responsable ", required=True)
    num_tel = fields.Integer("le numero responsable ", required=True)
    image = fields.Binary(string="entreprise image")
    pfe_id = fields.Many2one("pfe")

class BRANCHE(models.Model):
    _name = 'branche'

    specialite = fields.Char("donner la spécialité ", required=True)
    promo = fields.Char("donner la promo ", required=True)
    image = fields.Binary(string="branche image")
    pfe_id = fields.Many2one("pfe")
