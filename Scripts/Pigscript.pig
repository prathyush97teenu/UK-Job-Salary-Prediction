register '/usr/lib/pig/piggybank.jar';

define CSVExcelStorage org.apache.pig.piggybank.storage.CSVExcelStorage();

data1 = load 'gs://dataproc-staging-us-central1-950823520095-qwkpf0et/Train_rev1.xlsx' using CSVExcelStorage(',', 'YES_MULTILINE','NOCHANGE','SKIP_INPUT_HEADER') AS (Id:int, Title: chararray, FullDescription:chararray,LocationRaw:chararray,LocationNormalized:chararray,ContractType:chararray,ContractTime:chararray,Company:chararray,Category:chararray,SalaryRaw:chararray,SalaryNormalized:int,SourceName:chararray);

required_data = FOREACH data1 GENERATE Title AS Title, LocationNormalized AS Location, ContractType AS ContractType, ContractTime AS ContractTime, Company AS Company, Category AS Category, SalaryNormalized AS Salary;

contract_type_filter = FILTER required_data BY ContractType != 'NA';

contract_time_filter = FILTER contract_type_filter BY ContractTime != 'NA';

company_filter = FILTER contract_time_filter BY Company != 'NA';

STORE company_filter INTO 'gs://dataproc-staging-us-central1-950823520095-qwkpf0et/processed_train_data' USING org.apache.pig.piggybank.storage.CSVExcelStorage(',');

data2 = load 'gs://dataproc-staging-us-central1-950823520095-qwkpf0et/Test_rev1.xlsx' using CSVExcelStorage(',', 'YES_MULTILINE','NOCHANGE','SKIP_INPUT_HEADER') AS (Id:int, Title: chararray, FullDescription:chararray,LocationRaw:chararray,LocationNormalized:chararray,ContractType:chararray,ContractTime:chararray,Company:chararray,Category:chararray,SalaryRaw:chararray,SalaryNormalized:int,SourceName:chararray);

required_data_2 = FOREACH data2 GENERATE Title AS Title, LocationNormalized AS Location, ContractType AS ContractType, ContractTime AS ContractTime, Company AS Company, Category AS Category, SalaryNormalized AS Salary;

contract_type_filter_2 = FILTER required_data_2 BY ContractType != 'NA';

contract_time_filter_2 = FILTER contract_type_filter_2 BY ContractTime != 'NA';

company_filter_2 = FILTER contract_time_filter_2 BY Company != 'NA';

STORE company_filter_2 INTO 'gs://dataproc-staging-us-central1-950823520095-qwkpf0et/processed_test_data' USING org.apache.pig.piggybank.storage.CSVExcelStorage(',');