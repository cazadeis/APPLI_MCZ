#!/usr/bin/perl -w
     # Tell perl to send a html header.
     # So your browser gets the output
     # rather then <stdout>(command line
     # on the server.)
use CGI qw(:standard);
use strict;
use XML::LibXML;

 my $query = new CGI;
 my $valeur_vent2 = $query->param('Vent2'); #donnee d'entree "Vent2"
 my $filename = "parameters.xml";
 my $p = XML::LibXML->new();
 my $d = $p->parse_file($filename);

for my $node ($d->findnodes('//ParametersOfMCZ'))
{
   my ($vent2_node) = $node->findnodes('Ventilateur2/text()')
      or next;
   $vent2_node->setData($valeur_vent2);
}
print $d->toString; #Affiche
print $d->toFile($filename,0);
