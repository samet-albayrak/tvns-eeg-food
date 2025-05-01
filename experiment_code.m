if exist('s1')==1
    portmess=['Port s1 already open, attempting to close...'];
    disp(portmess);
    try
        fclose(s1);
        delete(s1);
        clear s1;
        portmess=['Port s1 succesfully closed'];
        disp(portmess);
    catch err
        disp('Port not successfully closed. You should restart Matlab')
    end    
end
clear;
warning('off','MATLAB:dispatcher:InexactMatch')
warning('off','MATLAB:dispatcher:InexactCaseMatch')

% begin experiment

config_io;
outp(20220, 0);

outp(20220, 20);
WaitSecs(0.001);
outp(20220, 0); 

%% collect information to save results from scale
ss = inputdlg('Enter participant number:',...
             'Number');
ss=ss{1,1};

condition_list = {'Lobe','Cymba','Tragus','CT','training'};
[condition,tf] = listdlg('PromptString',{'Select a condition:',...
    'Only one file can be selected at a time.',''},...
    'SelectionMode','single', 'ListString',condition_list);
sel_condition = condition_list{1,condition};

%% block rest 1, preparation section
block = 'During';
t=date;
DateString = datestr(t);
filename = [ss,'_',sel_condition,'_',block,'_',DateString,'.xlsx'];

%% begin block rest 1, "before sipping cortical oscillations"

%press any key to continue or sth like that
prompt ={'\fontsize{16} Plug participant electrodes and give instructions for \newline block 1: rest'};
opts.Interpreter = 'tex';
opts.Resize='on';
opts.WindowStyle='normal';
opts.Default = 'OK';
h = questdlg(prompt,'wait','OK','skip rest block 1',opts);

if strcmp(h,'OK')== 1
    % wait for user input
    h = warndlg('When you are ready, hit ok (when TENS light is off)','Wait...');
    uiwait(h);
    disp('300 s wait initiated');
    outp(20220, 21);
    WaitSecs(0.001);
    outp(20220, 0);

    % WaitSecs(300) %5min of resting state

    %% 5 min resting state with tvns starts marked

    s = daq.createSession('ni');
       try % assign channel and supress warning
            ch = addCounterInputChannel(s,'Dev1','ctr0','EdgeCount');
        catch
        end     

    %just to be safe, reset the counter
        try % reset counter and suppress error message
            startForeground(s);% seems to reset the counter, unlike resetcounters
        catch
        end

    %pre-allocate variables
    TENSblocktime = zeros(1,6);    
    k=1;     
    timecont=clock;%log start time of run

         WaitSecs(300); %5min of resting state

        display('end of rest block');
elseif strcmp(h,'skip rest block 1')== 1
    disp('rest block 1 skipped');
end
%% block sip preparation section
% prepare reading trigger from TENS device

%%press any key to continue or sth like that
prompt ={'\fontsize{16} Plug participant electrodes and give instructions for \newline block 2: sipping'};
opts.Interpreter = 'tex';
opts.Resize='on';
opts.WindowStyle='normal';
opts.Default = 'OK';
h = questdlg(prompt,'wait','OK','skip sip block',opts);

if strcmp(h,'OK')== 1
        display('Sip block preparations initialized');
    
      s = daq.createSession('ni');
       try % assign channel and supress warning
            ch = addCounterInputChannel(s,'Dev1','ctr0','EdgeCount');
        catch
        end     

    %just to be safe, reset the counter
        try % reset counter and suppress error message
            startForeground(s);% seems to reset the counter, unlike resetcounters
        catch
        end

% prepare audiofiles
    [r2,fs]=audioread('hazir.mp3');% load ready cue (to indicate start of sipping block)
    WaitSecs(.5);
    ready = audioplayer(r2, fs);

    %initialize serial for reading scale
        s1 = serial('com3','baudrate',9600,'terminator','CR');
        fopen(s1);

    %pre-allocate variables
    TENSblocktime = zeros(1,6);
    sipblocktime=zeros(1,6);
    siptime = zeros(1,55);
    foodweight = zeros(1,50);
    fw_mat=zeros(50,50);
    k=1;
    display('Sip block preparations finalized');
    h = warndlg('When you are ready, hit ok (when TENS light is off)','Wait...');
    uiwait(h);

%% experiment run section    
timecont=clock;%log start time of run
 m=0;
for j = 1:10
    %% wait for stimulator to start
    disp('waiting for TENS to start');
    start=inputSingleScan(s);%need to have one first to get the counter started right
        while start == 0
            start=inputSingleScan(s);
        end

    display('TENS started');
    TENSblocktime(j) = etime(clock,timecont);% log time
    
    if j==1
        outp(20220, 22);
        WaitSecs(0.001);
        outp(20220, 0); %marker for sip session start
    end    
    WaitSecs(29); % wait for tVNS block to end
    play(ready);% play sound to signal get ready
    display('sip block started');
    sipblocktime(j) = etime(clock,timecont); % log time
    
    WaitSecs(3); %this line gets ignored.  
    
            for i = 1:5
                    outp(20220, 25);
                    WaitSecs(0.001);
                    outp(20220, 0); %marker for events (sips)

                    beep;%play sound to signal to swallow
                    siptime(k) = etime(clock,timecont); % log time

                    k=k+1;
                    %WaitSecs(5);% give time to swallow
                    l=1;   
                    tic
                    while toc<=5
                        foodweight(l) = bal_read(s1);   
                        WaitSecs(0.05);
                        %fprintf('elapsed time is: %.2f seconds. \n',toc')
                        l=l+1;
                    end
            m=m+1;        
            fw_mat(:,m)=foodweight';
             end
        try % reset counter and suppress error message
            startForeground(s);
        catch
        end   
    end
    writematrix(fw_mat,filename);
elseif strcmp(h,'skip sip block')== 1
    display('sip block skipped');
end
%% after sipping

%press any key to continue or sth like that
prompt ={'\fontsize{16} Plug participant electrodes and give instructions for \newline block 3: rest'};
opts.Interpreter = 'tex';
opts.Resize='on';
opts.WindowStyle='normal';
opts.Default = 'OK';
h = questdlg(prompt,'wait','OK','skip rest block 2',opts);

if strcmp(h,'OK')== 1
    h = warndlg('When you are ready, hit ok (when TENS light is off)','Wait...');
    uiwait(h);
   disp('300 s wait initiated');
    outp(20220, 23);
    WaitSecs(0.001);
    outp(20220, 0);

% WaitSecs(300) %5min of resting state

%% 5 min resting state with tvns starts marked

s = daq.createSession('ni');
   try % assign channel and supress warning
        ch = addCounterInputChannel(s,'Dev1','ctr0','EdgeCount');
    catch
    end     
    
%just to be safe, reset the counter
    try % reset counter and suppress error message
        startForeground(s);% seems to reset the counter, unlike resetcounters
    catch
    end
       
%pre-allocate variables
TENSblocktime = zeros(1,6);    
k=1;     
timecont=clock;%log start time of run

         WaitSecs(300); %5min of resting state

display('end of rest block');
elseif strcmp(h,'skip rest block 2')== 1
    disp('rest block 2 skipped');
end

%% end block

outp(20220, 29);
WaitSecs(0.001);
outp(20220, 0);

display('end of during block');

outp(20220, 30);
WaitSecs(0.001);
outp(20220, 0); 
block = 'After';
t=date;
DateString = datestr(t);
filename = [ss,'_',sel_condition,'_',block,'_',DateString,'.xlsx'];

%% begin "after stimulation block 

%% cortical oscillations

%press any key to continue or sth like that
prompt ={'\fontsize{16} Unplug participant electrodes and give instructions for \newline  After stimulation block 1: rest'};
opts.Interpreter = 'tex';
opts.Resize='on';
opts.WindowStyle='normal';
opts.Default = 'OK';
h = questdlg(prompt,'wait','OK','skip after rest block 1',opts);

if strcmp(h,'OK')== 1
    % wait for user input
    disp('300 s wait initiated');
    outp(20220, 31);
    WaitSecs(0.001);
    outp(20220, 0);

    WaitSecs(300); %5min of resting state
    
elseif strcmp(h,'skip after rest block 1')== 1
    disp('After rest block 1 skipped');
end

outp(20220, 39);
WaitSecs(0.001);
outp(20220, 0);

display('end of after stimulation block');
if exist('s1')==1
    fclose(s1)
    delete(s1)
    clear s1
end