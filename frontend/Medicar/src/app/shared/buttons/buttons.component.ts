import { Component, Input, OnInit } from '@angular/core';

@Component({
  selector: 'app-buttons',
  templateUrl: './buttons.component.html',
  styleUrls: ['./buttons.component.scss']
})
export class ButtonsComponent implements OnInit {


  @Input()
  type: string = "";

  @Input()
  theme: "blue"|"white"|"small-blue"| "blue-background-none" |"simple" = "white";

  @Input()
  value: string = "";

  @Input()
  imageValue: string = "";


  constructor() { }

  ngOnInit(): void {
  }

  imageButton(){
    if(this.imageValue != '') {
      return true;
    }
    return false;
  }


  checkButtonStyle(){
    switch(this.theme){
      case "small-blue":
        return "button-small-blue";
        break;
      case "blue-background-none":
        return "button-blue-background-none";
        break;
      case "blue":

        return "button-blue";
        break;
      default:
        return "button-white";
        break;
    }
  }

}
