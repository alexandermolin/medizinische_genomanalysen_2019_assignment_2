#! /usr/bin/env python3

import vcf

__author__ = 'Alexander Molin'


class Assignment2:

    def __init__(self, file_name="chr22_new.vcf"):
        self.filename = file_name
        ## Check if pyvcf is installed
        print("PyVCF version: %s" % vcf.VERSION)
        # Create reader object
        self.total_num_var = self.get_total_number_of_variants_of_file()

    def get_total_number_of_variants_of_file(self):
        '''
        Get the total number of variants
        :return: total number of variants
        '''

        total_num_var = 0 #counter
        with open("chr22_new.vcf") as myVCF:
            vcf_reader = vcf.Reader(myVCF)
            for record in vcf_reader:
                total_num_var += 1
        print("Total number of variants is ", total_num_var)
        return total_num_var

    def get_average_quality_of_file(self):
        '''
        Get the average PHRED quality of all variants
        :return:
        '''

        sum_qual = 0
        with open("chr22_new.vcf") as myVCF:
            vcf_reader = vcf.Reader(myVCF)
            for record in vcf_reader:
                sum_qual = sum_qual + record.QUAL
        print("Average PHRED quality of the variants is ", round((sum_qual/self.total_num_var), 2))
        return sum_qual

    def get_variant_caller_of_vcf(self):
        '''
        Return the variant caller name
        :return:
        '''

        vcaller = []
        with open("chr22_new.vcf") as myVCF:
            vcf_reader = vcf.Reader(myVCF)
            for record in vcf_reader:
                vcaller = record.INFO['callsetnames']
        print("The variant caller of vcf is ", vcaller[1])

    def get_human_reference_version(self):
        '''
        Return the genome reference version
        :return:
        '''

        with open("chr22_new.vcf") as myVCF:
            vcf_reader = vcf.Reader(myVCF)
            for record in vcf_reader:
                info = record.INFO["difficultregion"]
                reference_version = info[0]
                print("The reference genome version is ", reference_version[0:4])
                break

    def get_number_of_indels(self):
        '''
        Return the number of identified INDELs
        :return:
        '''

        num_indel = 0 #indel counter
        with open("chr22_new.vcf") as myVCF:
            vcf_reader = vcf.Reader(myVCF)
            for record in vcf_reader:
                if record.is_indel:
                    num_indel += 1

        print("The number of indels is ", num_indel)
        return num_indel

    def get_number_of_snvs(self):
        '''
        Return the number of SNVs
        :return:
        '''

        num_snv = 0 #snv counter
        with open("chr22_new.vcf") as myVCF:
            vcf_reader = vcf.Reader(myVCF)
            for record in vcf_reader:
                if record.is_snp:
                    num_snv += 1
        print("The number of SNVs is ", num_snv)
        return num_snv

    def get_number_of_heterozygous_variants(self):
        '''
        Return the number of heterozygous variants
        :return:
        '''

        num_heteros = 0 #counter
        with open("chr22_new.vcf") as myVCF:
            vcf_reader = vcf.Reader(myVCF)
            for record in vcf_reader:
                num_heteros += record.num_het

        print("The number of heterozygous variants is ", num_heteros)

    def merge_chrs_into_one_vcf(self):
        '''
        Creates one VCF containing all variants of chr21 and chr22
        :return:
        '''
        file = open("chr21_new.vcf")
        w_f = open("mergedVCF_21_22.vcf", "w+")
        for line in file:
            w_f.write(line)
        file.close
        w_f.close

        file = open("chr22_new.vcf")
        w_f = open("mergedVCF_21_22.vcf", "a")
        for line in file:
            w_f.write(line)
        file.close
        w_f.close

        print("File with merged chr21 and chr22 is created.")

    def print_summary(self):
        self.get_average_quality_of_file()
        self.get_total_number_of_variants_of_file()
        self.get_variant_caller_of_vcf()
        self.get_human_reference_version()
        self.get_number_of_indels()
        self.get_number_of_snvs()
        self.get_number_of_heterozygous_variants()
        self.merge_chrs_into_one_vcf()

def main():
    print("Assignment 2")
    assignment2 = Assignment2()
    assignment2.print_summary()
    print("Done with assignment 2")


if __name__ == '__main__':
    main()
